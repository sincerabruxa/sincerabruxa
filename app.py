from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
import unicodedata
import logging
import datetime
import pytz
import os
from config import Config

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Mapeamento robusto de nomes de signos para slug da UOL
SIGNO_MAP = {
    'aries': 'aries', 'áries': 'aries', 'carneiro': 'aries',
    'touro': 'touro', 'taurus': 'touro',
    'gemeos': 'gemeos', 'gêmeos': 'gemeos', 'gemini': 'gemeos',
    'cancer': 'cancer', 'câncer': 'cancer', 'caranguejo': 'cancer',
    'leao': 'leao', 'leão': 'leao', 'leo': 'leao',
    'virgem': 'virgem', 'virgo': 'virgem',
    'libra': 'libra', 'balanca': 'libra', 'balança': 'libra',
    'escorpiao': 'escorpiao', 'escorpião': 'escorpiao', 'scorpio': 'escorpiao',
    'sagitario': 'sagitario', 'sagitário': 'sagitario', 'sagittarius': 'sagitario',
    'capricornio': 'capricornio', 'capricórnio': 'capricornio', 'capricorn': 'capricornio',
    'aquario': 'aquario', 'aquário': 'aquario', 'aquarius': 'aquario',
    'peixes': 'peixes', 'pisces': 'peixes'
}

# Buscar horóscopo do UOL (diário)
def get_horoscope_diario(signo):
    slug = SIGNO_MAP.get(
        unicodedata.normalize('NFKD', signo.strip().lower()).encode('ASCII', 'ignore').decode('ASCII')
    )
    if not slug:
        return "Signo não reconhecido."
    url = f"https://www.uol.com.br/universa/horoscopo/{slug}/horoscopo-do-dia/"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        horoscopo_section = soup.find('div', class_='horoscope-open-content')
        return horoscopo_section.get_text(strip=True) if horoscopo_section else "Horóscopo diário não encontrado."
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar horóscopo diário para {signo}: {e}")
        return "Erro ao acessar o horóscopo diário."

# Buscar horóscopo semanal (exemplo usando site alternativo)
def get_horoscopo_semanal(signo):
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
        "aquario": "aquario"
    }
    slug = SIGNO_MAP.get(
        unicodedata.normalize('NFKD', signo.strip().lower()).encode('ASCII', 'ignore').decode('ASCII')
    )
    if not slug:
        return f"Signo '{signo}' não reconhecido ou não disponível."
    signo_formatado = signos_para_url.get(slug)
    if not signo_formatado:
        return f"Signo '{signo}' não reconhecido ou não disponível."
    url = f"https://merlim.pt/previsao-signo-{signo_formatado}/"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        horoscopo_section = soup.find('div', class_='horoscope-container')
        if horoscopo_section:
            return horoscopo_section.get_text(strip=True)
        else:
            return f"Horóscopo semanal para {signo.capitalize()} não encontrado."
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar horóscopo semanal para {signo.capitalize()}: {e}")
        return f"Erro ao acessar o horóscopo semanal para {signo.capitalize()}."

# Calcular fase da lua (sem scraping)
def get_fase_lua():
    try:
        agora = datetime.datetime.now(pytz.utc)
        timestamp = int(agora.timestamp())
        lunation = 2551443  # duração de uma lunação em segundos
        desde_lua_nova = timestamp - 592500000  # referência antiga de lua nova
        fase = (desde_lua_nova % lunation) / lunation
        if fase < 0.03 or fase > 0.97:
            return "Lua Nova 🌑"
        elif fase < 0.25:
            return "Lua Crescente 🌒"
        elif fase < 0.27:
            return "Quarto Crescente 🌓"
        elif fase < 0.47:
            return "Lua Gibosa Crescente 🌔"
        elif fase < 0.53:
            return "Lua Cheia 🌕"
        elif fase < 0.75:
            return "Lua Gibosa Minguante 🌖"
        elif fase < 0.77:
            return "Quarto Minguante 🌗"
        else:
            return "Lua Minguante 🌘"
    except Exception as e:
        print(f"Erro ao calcular fase da lua: {e}")
        return "Erro ao acessar o calendário lunar."

@app.route('/', methods=['GET', 'POST'])
def index():
    """Página principal"""
    horoscopo_diario = "Sintonize-se com o horóscopo do dia e descubra os sinais que o universo envia ao seu coração."
    horoscopo_semanal = "Escolha seu signo e tipo de horóscopo para ver a previsão semanal."
    signo = ""
    fase_lua = get_fase_lua()
    
    if request.method == 'POST':
        signo = request.form.get("signo")
        if signo:
            horoscopo_diario = get_horoscope_diario(signo)
            horoscopo_semanal = get_horoscopo_semanal(signo)
            print(f"Horóscopo semanal para {signo}: {horoscopo_semanal}")
    
    return render_template(
        'index.html',
        horoscopo_diario=horoscopo_diario,
        horoscopo_semanal=horoscopo_semanal,
        signo=signo,
        fase_lua=fase_lua,
        signos_select=Config.get_signos_select(),
        parcerias=Config.PARCERIAS,
        servicos=Config.SERVICOS,
        depoimentos=Config.DEPOIMENTOS,
        midias_sociais=Config.MIDIAS_SOCIAIS
    )

@app.route('/horoscopo', methods=['POST'])
def horoscopo_api():
    signo = request.json.get('signo')
    if not signo:
        return jsonify({'erro': 'Signo não informado.'}), 400
    horoscopo_diario = get_horoscope_diario(signo)
    return jsonify({'horoscopo_diario': horoscopo_diario})

@app.errorhandler(404)
def not_found(error):
    """Página 404 personalizada"""
    return render_template('index.html', 
                         horoscopo_diario="Página não encontrada. Volte ao início.",
                         horoscopo_semanal="",
                         signo="",
                         fase_lua=get_fase_lua(),
                         signos_select=Config.get_signos_select(),
                         parcerias=Config.PARCERIAS,
                         servicos=Config.SERVICOS,
                         depoimentos=Config.DEPOIMENTOS,
                         midias_sociais=Config.MIDIAS_SOCIAIS), 404

@app.errorhandler(500)
def internal_error(error):
    """Página 500 personalizada"""
    return render_template('index.html',
                         horoscopo_diario="Erro interno do servidor. Tente novamente.",
                         horoscopo_semanal="",
                         signo="",
                         fase_lua=get_fase_lua(),
                         signos_select=Config.get_signos_select(),
                         parcerias=Config.PARCERIAS,
                         servicos=Config.SERVICOS,
                         depoimentos=Config.DEPOIMENTOS,
                         midias_sociais=Config.MIDIAS_SOCIAIS), 500

if __name__ == '__main__':
    app.run(debug=Config.DEBUG, 
            host=Config.HOST, 
            port=Config.PORT) 