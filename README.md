# A Sincera Bruxa - Tarot & Espiritualidade

Site de consultas de tarot e orientação espiritual desenvolvido com Flask e Tailwind CSS.

## Funcionalidades

- **Horóscopo Diário**: Consulta horóscopo do dia para todos os signos
- **Horóscopo Semanal**: Previsões semanais personalizadas
- **Fase da Lua**: Informações sobre a fase atual da lua
- **Serviços Espirituais**: Apresentação dos serviços oferecidos

## Tecnologias Utilizadas

- **Backend**: Python Flask
- **Frontend**: HTML, Tailwind CSS, JavaScript
- **Web Scraping**: BeautifulSoup4 para buscar horóscopos
- **Deploy**: Render

## Estrutura do Projeto

```
tatiana/
├── app.py                 # Aplicação Flask principal
├── requirements.txt       # Dependências Python
├── Procfile              # Configuração para deploy
├── runtime.txt           # Versão do Python
├── templates/
│   └── index.html        # Template principal
├── static/
│   ├── assets/           # Arquivos estáticos
│   ├── img/              # Imagens
│   └── js/               # JavaScript
└── README.md             # Este arquivo
```

## Deploy no Render

### Passos para Deploy:

1. **Criar conta no Render**:
   - Acesse [render.com](https://render.com)
   - Faça login ou crie uma conta

2. **Conectar repositório**:
   - Clique em "New +" → "Web Service"
   - Conecte seu repositório GitHub/GitLab
   - Selecione o repositório do projeto

3. **Configurar o serviço**:
   - **Name**: `a-sincera-bruxa` (ou nome de sua preferência)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free (ou pago se necessário)

4. **Variáveis de Ambiente** (opcional):
   - Não são necessárias para este projeto

5. **Deploy**:
   - Clique em "Create Web Service"
   - Aguarde o build e deploy automático

### Arquivos de Configuração

- **`Procfile`**: Especifica como executar a aplicação
- **`requirements.txt`**: Lista as dependências Python
- **`runtime.txt`**: Define a versão do Python
- **`.gitignore`**: Evita envio de arquivos desnecessários

## Desenvolvimento Local

### Instalação:

```bash
# Clonar o repositório
git clone <url-do-repositorio>
cd tatiana

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt

# Executar aplicação
python app.py
```

### Acessar:
- Abra o navegador e acesse: `http://localhost:5000`

## Funcionalidades Técnicas

### Web Scraping
- **Horóscopo Diário**: Busca no UOL
- **Horóscopo Semanal**: Busca em site alternativo
- **Tratamento de Erros**: Fallbacks para casos de indisponibilidade

### Cálculo da Fase da Lua
- Algoritmo matemático para calcular a fase atual
- Não depende de APIs externas

### Interface Responsiva
- Design adaptável para mobile e desktop
- Animações suaves e efeitos visuais
- Paleta de cores mística (índigo/amarelo)

## Manutenção

### Atualizações:
- O site busca horóscopos em tempo real
- Não requer atualizações manuais de conteúdo

### Monitoramento:
- Logs disponíveis no painel do Render
- Status do serviço visível no dashboard

## Contato

Para dúvidas sobre o projeto ou melhorias, entre em contato através do site.

---

**Desenvolvido com ❤️ para A Sincera Bruxa** 