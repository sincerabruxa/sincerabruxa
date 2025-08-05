import os
from datetime import datetime

class Config:
    """Configurações do projeto"""
    
    # Configurações básicas
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'
    
    # Configurações do servidor
    HOST = os.environ.get('HOST', '0.0.0.0')
    PORT = int(os.environ.get('PORT', 5000))
    
    # Configurações de horóscopo
    HOROSCOPE_API_URL = os.environ.get('HOROSCOPE_API_URL', 'https://horoscope-api.herokuapp.com/horoscope')
    
    # Configurações de fase lunar
    MOON_PHASE_API_URL = os.environ.get('MOON_PHASE_API_URL', 'https://www.farmsense.net/v1/moonphases/')
    
    # Configurações de signos
    SIGNOS = {
        'aries': 'Áries',
        'taurus': 'Touro', 
        'gemini': 'Gêmeos',
        'cancer': 'Câncer',
        'leo': 'Leão',
        'virgo': 'Virgem',
        'libra': 'Libra',
        'scorpio': 'Escorpião',
        'sagittarius': 'Sagitário',
        'capricorn': 'Capricórnio',
        'aquarius': 'Aquário',
        'pisces': 'Peixes'
    }
    
    # Configurações de parcerias
    PARCERIAS = [
        {
            'nome': 'Casa Mística',
            'descricao': 'Especialistas em cristais, incensos e produtos místicos para complementar sua jornada espiritual.',
            'url': 'https://casamistica.com.br',
            'imagem': 'parcerias.svg'
        },
        {
            'nome': 'Espaço Zen',
            'descricao': 'Centro de bem-estar e meditação, oferecendo terapias holísticas e cursos de autoconhecimento.',
            'url': 'https://espacozensp.com.br',
            'imagem': 'parcerias.svg'
        }
    ]
    
    # Configurações de serviços
    SERVICOS = [
        {
            'nome': 'Tarot Completo',
            'descricao': 'Leitura completa com 21 cartas para visão geral da sua vida atual e futura.',
            'preco': 89,
            'icone': '🃏'
        },
        {
            'nome': 'Amor & Relacionamentos',
            'descricao': 'Foco específico em questões amorosas, relacionamentos e vida afetiva.',
            'preco': 65,
            'icone': '💝'
        },
        {
            'nome': 'Carreira & Finanças',
            'descricao': 'Orientação para decisões profissionais e questões financeiras importantes.',
            'preco': 65,
            'icone': '💼'
        }
    ]
    
    # Configurações de depoimentos
    DEPOIMENTOS = [
        {
            'nome': 'Maria Silva',
            'inicial': 'M',
            'texto': '"Leitura incrível! Luna me ajudou a entender questões que eu carregava há anos. Recomendo muito!"',
            'estrelas': 5
        },
        {
            'nome': 'João Santos',
            'inicial': 'J',
            'texto': '"Consulta muito esclarecedora sobre minha carreira. As orientações foram fundamentais para minha decisão."',
            'estrelas': 5
        },
        {
            'nome': 'Ana Costa',
            'inicial': 'A',
            'texto': '"Luna tem uma sensibilidade única. Suas leituras são sempre certeiras e transformadoras."',
            'estrelas': 5
        }
    ]
    
    # Configurações de mídias sociais
    MIDIAS_SOCIAIS = [
        {
            'plataforma': 'YouTube',
            'url': 'https://www.youtube.com/watch?v=sc1RIX0RZBo',
            'embed_url': 'https://www.youtube.com/embed/sc1RIX0RZBo',
            'icone': '📺',
            'cor': 'from-red-600 to-red-700'
        },
        {
            'plataforma': 'TikTok',
            'url': 'https://www.tiktok.com/@watechevoce/video/7524863455111712006',
            'embed_id': '7524863455111712006',
            'icone': '🎵',
            'cor': 'from-pink-600 to-purple-600'
        },
        {
            'plataforma': 'Instagram',
            'url': 'https://www.instagram.com/reel/DI22kizqeNK/?utm_source=ig_embed',
            'embed_id': 'DI22kizqeNK',
            'icone': '📸',
            'cor': 'from-pink-600 to-purple-600'
        }
    ]
    
    @staticmethod
    def get_fase_lua():
        """Retorna a fase atual da lua"""
        # Implementação simplificada - em produção usar API real
        fases = ['Lua Nova', 'Lua Crescente', 'Lua Cheia', 'Lua Minguante']
        return fases[datetime.now().day % 4]
    
    @staticmethod
    def get_signos_select():
        """Retorna lista de signos para o select"""
        return [(slug, nome) for slug, nome in Config.SIGNOS.items()] 