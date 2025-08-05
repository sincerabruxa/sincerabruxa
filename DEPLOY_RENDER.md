# Guia de Deploy no Render - A Sincera Bruxa

## 📋 Pré-requisitos

1. **Conta no Render**: [render.com](https://render.com)
2. **Repositório Git**: GitHub, GitLab ou Bitbucket
3. **Projeto configurado**: Todos os arquivos de configuração já estão prontos

## 🚀 Passos para Deploy

### 1. Preparar o Repositório

Certifique-se de que todos estes arquivos estão no seu repositório:

```
tatiana/
├── app.py                 ✅ Aplicação Flask
├── requirements.txt       ✅ Dependências Python
├── Procfile              ✅ Configuração do Render
├── runtime.txt           ✅ Versão do Python
├── render.yaml           ✅ Configuração automática
├── .gitignore            ✅ Arquivos ignorados
├── templates/
│   └── index.html        ✅ Template principal
└── static/               ✅ Arquivos estáticos
```

### 2. Criar Serviço no Render

1. **Acesse o Render**: [dashboard.render.com](https://dashboard.render.com)
2. **Clique em "New +"** → **"Web Service"**
3. **Conecte seu repositório**:
   - Escolha GitHub/GitLab/Bitbucket
   - Selecione o repositório do projeto
   - Clique em "Connect"

### 3. Configurar o Serviço

**Configurações básicas:**
- **Name**: `a-sincera-bruxa` (ou nome de sua preferência)
- **Environment**: `Python 3`
- **Region**: Escolha a mais próxima (ex: US East)
- **Branch**: `main` (ou sua branch principal)

**Configurações avançadas:**
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`
- **Plan**: `Free` (ou pago se necessário)

### 4. Deploy Automático

1. **Clique em "Create Web Service"**
2. **Aguarde o build** (pode levar 2-5 minutos)
3. **Verifique os logs** se houver problemas

### 5. Verificar o Deploy

Após o deploy, você receberá uma URL como:
`https://a-sincera-bruxa.onrender.com`

**Teste as funcionalidades:**
- ✅ Página carrega corretamente
- ✅ Horóscopo funciona
- ✅ Fase da lua aparece
- ✅ Design responsivo

## 🔧 Configurações Importantes

### Variáveis de Ambiente
Para este projeto, **não são necessárias** variáveis de ambiente.

### Domínio Personalizado (Opcional)
1. Vá em **Settings** → **Custom Domains**
2. Adicione seu domínio
3. Configure o DNS conforme instruções

### Monitoramento
- **Logs**: Disponível em **Logs** no painel
- **Status**: Verificado automaticamente
- **Uptime**: Monitorado pelo Render

## 🐛 Solução de Problemas

### Erro de Build
```
Error: Could not find a version that satisfies the requirement
```
**Solução**: Verifique se o `requirements.txt` está correto

### Erro de Start
```
Error: No module named 'flask'
```
**Solução**: Verifique se o `Procfile` está correto

### Página não carrega
**Verifique**:
1. Logs no painel do Render
2. URL está correta
3. Serviço está "Live"

### Horóscopo não funciona
**Possíveis causas**:
1. Sites externos indisponíveis
2. Rate limiting
3. Mudanças nos sites fonte

## 📊 Monitoramento

### Logs Importantes
- **Build logs**: Durante o deploy
- **Runtime logs**: Durante execução
- **Error logs**: Para debug

### Métricas
- **Uptime**: Disponível no dashboard
- **Response time**: Monitorado automaticamente
- **Error rate**: Alertas automáticos

## 🔄 Atualizações

### Deploy Automático
- Push para `main` = deploy automático
- Branch protection recomendada

### Deploy Manual
1. Vá em **Manual Deploy**
2. Escolha a branch
3. Clique em **Deploy**

## 📞 Suporte

### Render Support
- [Documentação oficial](https://render.com/docs)
- [Status page](https://status.render.com)

### Projeto
- Verifique os logs primeiro
- Teste localmente antes do deploy
- Use branches para testes

---

**✅ Projeto configurado e pronto para deploy!** 