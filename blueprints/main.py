import datetime
import json
import logging
import time
import unicodedata
from collections.abc import Callable
from functools import wraps
from typing import Any, Final, ParamSpec, TypeVar

import pytz
import requests
from bs4 import BeautifulSoup
from flask import Blueprint, jsonify, render_template, request

from config import Config
main_bp = Blueprint("main", __name__)

logger = logging.getLogger(__name__)

P = ParamSpec("P")
T = TypeVar("T")


def ttl_cache(ttl_seconds: int, cache_none: bool = False) -> Callable[[Callable[P, T]], Callable[P, T]]:
    """Cache simples com TTL. Por padrão, não armazena resultados None (falhas)."""

    def decorator(func: Callable[P, T]) -> Callable[P, T]:
        cache: dict[Any, tuple[float, T]] = {}

        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T: # type: ignore
            key = (args, frozenset(kwargs.items()))
            now = time.monotonic()
            expires, cached_value = cache.get(key, (0.0, None))  # type: ignore[misc]
            if now < expires and cached_value is not None:
                return cached_value

            value = func(*args, **kwargs)
            if cache_none or value is not None:
                cache[key] = (now + ttl_seconds, value)
            return value

        return wrapper

    return decorator

REQUEST_TIMEOUT: Final[int] = 10

REQUEST_HEADERS: Final[dict[str, str]] = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/119.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Referer": "https://www.uol.com.br/universa/horoscopo/",
    "Cache-Control": "no-cache",
}

# sessão HTTP reutilizável para reduzir overhead de conexões
session = requests.Session()
session.headers.update(REQUEST_HEADERS)

# Mapeamento robusto de nomes de signos para slug da UOL
SIGNO_MAP: Final[dict[str, str]] = {
    "aries": "aries",
    "áries": "aries",
    "carneiro": "aries",
    "touro": "touro",
    "taurus": "touro",
    "gemeos": "gemeos",
    "gêmeos": "gemeos",
    "gemini": "gemeos",
    "cancer": "cancer",
    "câncer": "cancer",
    "caranguejo": "cancer",
    "leao": "leao",
    "leão": "leao",
    "leo": "leao",
    "virgem": "virgem",
    "virgo": "virgem",
    "libra": "libra",
    "balanca": "libra",
    "balança": "libra",
    "escorpiao": "escorpiao",
    "escorpião": "escorpiao",
    "scorpio": "escorpiao",
    "sagitario": "sagitario",
    "sagitário": "sagitario",
    "sagittarius": "sagitario",
    "capricornio": "capricornio",
    "capricórnio": "capricornio",
    "capricorn": "capricornio",
    "aquario": "aquario",
    "aquário": "aquario",
    "aquarius": "aquario",
    "peixes": "peixes",
    "pisces": "peixes",
}


def _normalizar_signo(signo: str) -> str | None:
    if not signo:
        return None
    slug = unicodedata.normalize("NFKD", signo.strip().lower()).encode("ASCII", "ignore").decode("ASCII")
    return SIGNO_MAP.get(slug)


@ttl_cache(ttl_seconds=1800)  
def get_horoscopo_diario(signo: str) -> str | None:
    """Retorna o horóscopo do dia ou None se falhar."""
    slug = _normalizar_signo(signo)
    if not slug:
        return None

    url = f"https://www.uol.com.br/universa/horoscopo/{slug}/horoscopo-do-dia/"
    try:
        response = session.get(url, timeout=REQUEST_TIMEOUT)
        logger.info("UOL Scraping [%s]: Status %s, Tamanho: %d bytes", signo, response.status_code, len(response.text))
        
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        selectors = [
            "div.horoscope-open-content",
            "div.horoscope-content",
            "article[data-testid='content']",
            "article",
            "div[data-testid='content']",
        ]

        for selector in selectors:
            container = soup.select_one(selector)
            if not container:
                continue

            paragraphs = container.find_all(["p", "span"])
            text_parts = [p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)]
            if text_parts:
                return " ".join(text_parts)

            raw_text = container.get_text(strip=True)
            if raw_text:
                return raw_text

        next_data_script = soup.find("script", id="__NEXT_DATA__")
        if next_data_script and next_data_script.string:
            try:
                json_data = json.loads(next_data_script.string)
                extracted = _extract_text_from_next_data(json_data)
                if extracted:
                    return extracted
            except json.JSONDecodeError as err:
                logger.warning("Não foi possível decodificar JSON do Next.js: %s", err)

        return "Horóscopo diário não encontrado."
    except requests.exceptions.RequestException as exc:
        status = getattr(exc.response, "status_code", None)
        logger.exception("Erro ao buscar horóscopo diário para %s (status=%s)", signo, status)
        return "Erro ao acessar o horóscopo diário."


@ttl_cache(ttl_seconds=60 * 60 * 12)  # caching mais longo pois previsão semanal muda com menor frequência
def get_horoscopo_semanal(signo: str) -> str:
    signos_para_url = {
        "balanca": "libra",
        "virgem": "virgem",
        "capricornio": "capricornio",
        "escorpiao": "escorpiao",
        "caranguejo": "cancer",
        "peixes": "peixes",
        "carneiro": "aries",
        "leao": "leao",
        "touro": "touro",
        "gemeos": "gemeos",
        "sagitario": "sagitario",
        "aquario": "aquario",
    }
    slug = _normalizar_signo(signo)
    if not slug:
        return f"Signo '{signo}' não reconhecido ou não disponível."

    signo_formatado = signos_para_url.get(slug)
    if not signo_formatado:
        return f"Signo '{signo}' não reconhecido ou não disponível."

    url = f"https://merlim.pt/previsao-signo-{signo_formatado}/"
    try:
        response = session.get(url, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        horoscopo_section = soup.find("div", class_="horoscope-container")
        if horoscopo_section:
            return horoscopo_section.get_text(strip=True)
        return f"Horóscopo semanal para {signo.capitalize()} não encontrado."
    except requests.exceptions.RequestException:
        logger.exception("Erro ao buscar horóscopo semanal para %s", signo)
        return f"Erro ao acessar o horóscopo semanal para {signo.capitalize()}."


@ttl_cache(ttl_seconds=3600)
def get_fase_lua() -> str:
    try:
        agora = datetime.datetime.now(pytz.utc)
        timestamp = int(agora.timestamp())
        lunation = 2551443  # duração de uma lunação em segundos
        desde_lua_nova = timestamp - 592500000  # referência antiga de lua nova
        fase = (desde_lua_nova % lunation) / lunation

        if fase < 0.03 or fase > 0.97:
            return "Lua Nova 🌑"
        if fase < 0.25:
            return "Lua Crescente 🌒"
        if fase < 0.27:
            return "Quarto Crescente 🌓"
        if fase < 0.47:
            return "Lua Gibosa Crescente 🌔"
        if fase < 0.53:
            return "Lua Cheia 🌕"
        if fase < 0.75:
            return "Lua Gibosa Minguante 🌖"
        if fase < 0.77:
            return "Quarto Minguante 🌗"
        return "Lua Minguante 🌘"
    except Exception:  # noqa: BLE001 - queremos capturar qualquer exceção inesperada
        logger.exception("Erro ao calcular fase da lua")
        return "Erro ao acessar o calendário lunar."


@main_bp.route("/", methods=["GET", "POST"])
def index():
    """Página principal."""
    horoscopo_diario = (
        "Sintonize-se com o horóscopo do dia e descubra os sinais que o universo envia ao seu coração."
    )
    horoscopo_semanal = "Escolha seu signo e tipo de horóscopo para ver a previsão semanal."
    signo = ""
    fase_lua = get_fase_lua()
    signo_consulta = ""
    signo_consulta_label = ""

    if request.method == "POST":
        signo = request.form.get("signo")
        if signo:
            horoscopo_diario = get_horoscopo_diario(signo)
            horoscopo_semanal = get_horoscopo_semanal(signo)
            logger.info("Horóscopo semanal para %s: %s", signo, horoscopo_semanal)
            signo_consulta = signo
            signo_consulta_label = Config.SIGNOS.get(signo, signo.capitalize())

    return render_template(
        "index.html",
        horoscopo_diario=horoscopo_diario,
        horoscopo_semanal=horoscopo_semanal,
        signo="",
        signo_consulta=signo_consulta,
        signo_consulta_label=signo_consulta_label,
        fase_lua=fase_lua,
        signos_select=Config.get_signos_select(),
        parcerias=Config.PARCERIAS,
        servicos=Config.SERVICOS,
        depoimentos=Config.DEPOIMENTOS,
        midias_sociais=Config.MIDIAS_SOCIAIS,
    )


@main_bp.route("/horoscopo", methods=["POST"])
def horoscopo_api():
    signo = request.json.get("signo") if request.is_json else request.form.get("signo")
    if not signo:
        return jsonify({"erro": "Signo não informado."}), 400
    horoscopo_diario = get_horoscopo_diario(signo)
    return jsonify({"horoscopo_diario": horoscopo_diario})


@main_bp.app_errorhandler(404)
def not_found(error):  # noqa: ARG001 - parâmetro exigido pelo Flask
    """Página 404 personalizada."""
    return (
        render_template(
            "index.html",
            horoscopo_diario="Página não encontrada. Volte ao início.",
            horoscopo_semanal="",
            signo="",
            fase_lua=get_fase_lua(),
            signos_select=Config.get_signos_select(),
            parcerias=Config.PARCERIAS,
            servicos=Config.SERVICOS,
            depoimentos=Config.DEPOIMENTOS,
            midias_sociais=Config.MIDIAS_SOCIAIS,
        ),
        404,
    )


@main_bp.app_errorhandler(500)
def internal_error(error):  # noqa: ARG001 - parâmetro exigido pelo Flask
    """Página 500 personalizada."""
    return (
        render_template(
            "index.html",
            horoscopo_diario="Erro interno do servidor. Tente novamente.",
            horoscopo_semanal="",
            signo="",
            fase_lua=get_fase_lua(),
            signos_select=Config.get_signos_select(),
            parcerias=Config.PARCERIAS,
            servicos=Config.SERVICOS,
            depoimentos=Config.DEPOIMENTOS,
            midias_sociais=Config.MIDIAS_SOCIAIS,
        ),
        500,
    )


def _extract_text_from_next_data(data: dict) -> str | None:
    """Procura conteúdo textual relevante dentro da árvore Next.js."""
    if not isinstance(data, (dict, list)):
        return None

    candidate_texts: list[str] = []

    def walk(node):
        if isinstance(node, dict):
            if node.get("type") in {"paragraph", "text"} and "content" in node:
                text_content = _join_content(node["content"])
                if text_content:
                    candidate_texts.append(text_content)
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(data)

    joined = " ".join(candidate_texts).strip()
    return joined or None


def _join_content(content):
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, list):
        parts = [_join_content(item) for item in content]
        return " ".join(part for part in parts if part)
    if isinstance(content, dict):
        value = content.get("text") or content.get("content")
        return _join_content(value)
    return ""
