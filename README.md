# A Sincera Bruxa - Site Místico

Site profissional para consultas de tarot e orientação espiritual, desenvolvido com Flask e design místico moderno.

## ✨ Características

- **Design Místico**: Interface elegante com gradientes, partículas animadas e efeitos visuais
- **Horóscopo Interativo**: Consulta de horóscopo em tempo real
- **Fase Lunar**: Exibição da fase atual da lua
- **Seção de Parcerias**: Apresentação de parceiros comerciais
- **Responsivo**: Funciona perfeitamente em mobile e desktop
- **Performance Otimizada**: Código refatorado e organizado

## 🏗️ Arquitetura Refatorada

### Estrutura de Arquivos

```
tatiana/
├── app.py                 # Aplicação Flask principal
├── config.py             # Configurações centralizadas
├── requirements.txt      # Dependências Python
├── static/
│   ├── css/
│   │   └── style.css    # Estilos CSS organizados
│   ├── js/
│   │   └── main.js      # JavaScript modularizado
│   └── img/             # Imagens e assets
├── templates/
│   └── index.html       # Template principal
└── README.md            # Documentação
```

### Melhorias Implementadas

#### 1. **Separação de Responsabilidades**
- **CSS externo**: `static/css/style.css` - Todos os estilos organizados
- **JavaScript modular**: `static/js/main.js` - Funcionalidades separadas
- **Configuração centralizada**: `config.py` - Configurações em um local

#### 2. **Organização do Código**
- **Configurações**: Centralizadas em `Config` class
- **Dados estáticos**: Parcerias, serviços, depoimentos em configuração
- **Funções modulares**: JavaScript organizado em funções específicas

#### 3. **Manutenibilidade**
- **Código limpo**: Sem scripts inline no HTML
- **Reutilização**: Componentes CSS e JS reutilizáveis
- **Documentação**: Código bem documentado

## 🚀 Instalação e Execução

### Pré-requisitos
- Python 3.8+
- pip

### Instalação

1. **Clone o repositório**
```bash
git clone <repository-url>
cd tatiana
```

2. **Instale as dependências**
```bash
pip install -r requirements.txt
```

3. **Execute a aplicação**
```bash
python app.py
```

4. **Acesse o site**
```
http://localhost:5000
```

## 🎨 Funcionalidades

### Seções Principais

1. **Hero Section**: Apresentação principal com call-to-action
2. **Horóscopo**: Consulta interativa de horóscopo por signo
3. **Fase da Lua**: Exibição da fase lunar atual
4. **Sobre**: Informações sobre a taróloga
5. **Serviços**: Tipos de consultas oferecidas
6. **Depoimentos**: Testemunhos de clientes
7. **Mídias Sociais**: Links para redes sociais
8. **Parcerias**: Seção de parceiros comerciais

### Efeitos Visuais

- **Partículas místicas**: Animações de sol, lua e estrelas
- **Gradientes animados**: Backgrounds com movimento
- **Fade-in sections**: Animações ao rolar
- **Hover effects**: Interações suaves
- **Glassmorphism**: Efeito de vidro translúcido

## 🔧 Configuração

### Variáveis de Ambiente

```bash
# Configurações básicas
SECRET_KEY=your-secret-key
DEBUG=True
HOST=0.0.0.0
PORT=5000

# APIs (opcional)
HOROSCOPE_API_URL=https://horoscope-api.herokuapp.com/horoscope
MOON_PHASE_API_URL=https://www.farmsense.net/v1/moonphases/
```

### Personalização

#### Adicionar Nova Parceria
```python
# Em config.py
PARCERIAS = [
    {
        'nome': 'Nova Parceria',
        'descricao': 'Descrição da parceria',
        'url': 'https://exemplo.com',
        'imagem': 'logo.svg'
    }
]
```

#### Modificar Serviços
```python
# Em config.py
SERVICOS = [
    {
        'nome': 'Novo Serviço',
        'descricao': 'Descrição do serviço',
        'preco': 100,
        'icone': '🔮'
    }
]
```

## 📱 Responsividade

O site é totalmente responsivo e funciona em:
- **Desktop**: Layout completo com todas as seções
- **Tablet**: Layout adaptado para telas médias
- **Mobile**: Menu hambúrguer e layout otimizado

## 🎯 Performance

### Otimizações Implementadas

1. **CSS externo**: Carregamento otimizado
2. **JavaScript modular**: Código organizado e eficiente
3. **Imagens otimizadas**: Formatos WebP e SVG
4. **Lazy loading**: Carregamento sob demanda
5. **Minificação**: Arquivos compactados

## 🔮 Tecnologias Utilizadas

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Tailwind CSS
- **Animações**: CSS3 + JavaScript
- **APIs**: Requests para horóscopo e fase lunar
- **Deploy**: Render (configurado)

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 🤝 Contribuição

Contribuições são bem-vindas! Por favor:

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📞 Contato

- **Email**: luna@mysticatarot.com
- **Telefone**: +55 22 98173-5681
- **Instagram**: @lunamystica

---

**Desenvolvido com 💜 e energia mística** 