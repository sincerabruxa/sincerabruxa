import os
from datetime import datetime

class Config:
    """Configurações do projeto"""
    
    # Configurações básicas
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'
    
    # Configurações do servidor
    HOST = "127.0.0.1"
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
            'slug': 'watech',
            'nome': 'WATech',
            'tagline': '',
            'descricao': (
                "A WAtech conecta negócios místicos ao mundo digital com tecnologia sob medida, design inteligente e suporte dedicado."
            ),
            'beneficios': [
                {'icone': '🌐', 'texto': 'Conectamos sua marca ao mundo digital com soluções tecnológicas personalizadas.'},
                {'icone': '💡', 'texto': 'Criamos sites, landing pages e lojas virtuais focadas em performance, SEO e conversão.'},
                {'icone': '🚀', 'texto': 'Tecnologia de ponta, design inteligente e suporte especializado para manter sua presença online atualizada.'},
                {'icone': '🛍️', 'texto': 'Descubra ferramentas e produtos selecionados em nossa vitrine Amazon oficial.'},
            ],
            'badge_label': 'Afiliado Amazon oficial',
            'url': 'https://www.watechevoce.com.br',
            'imagem': 'parceria1.png',
            'cta': 'Quero conhecer a WATech',
            'amazon_url': 'https://www.watechevoce.com.br/loja',
            'amazon_cta': 'Visitar nossa loja Amazon oficial'
        },
        {
            'nome': 'Parceria com A Sincera Bruxa',
            'descricao': (
                "Sua marca pode caminhar ao lado da A Sincera Bruxa em experiências que unem espiritualidade, bem-estar e tecnologia. "
                "Estamos em busca de parceiros que acreditam em conexões verdadeiras e desejam amplificar sua presença digital com uma audiência engajada."
            ),
            'url': 'https://wa.me/5522981735681?text=Olá%20A%20Sincera%20Bruxa!%20Quero%20conversar%20sobre%20parcerias.',
            'imagem': 'parcerias.svg',
            'cta': 'Iniciar conversa'
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
        },
        {
            'nome': 'Carla Mendes',
            'inicial': 'C',
            'texto': '"A consulta foi muito clara e acolhedora. Saí com respostas e mais confiança no meu caminho."',
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
            'url': 'https://www.tiktok.com/@watechevoce/video/7527100479894709509',
            'embed_id': '7527100479894709509',
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
        return sorted(((slug, nome) for slug, nome in Config.SIGNOS.items()), key=lambda item: item[1])