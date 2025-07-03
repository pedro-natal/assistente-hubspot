# Assistente HubSpot

Assistente inteligente integrado com HubSpot usando Streamlit e n8n.

## 🚀 Deploy Rápido

### Streamlit Cloud (Recomendado - GRÁTIS)

1. **Suba para GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy:** https://share.streamlit.io
3. **Configure:** `N8N_WEBHOOK_URL` nas secrets

**Veja o guia completo:** [DEPLOY_GUIDE.md](DEPLOY_GUIDE.md)

## �️ Desenvolvimento Local

### 1. Instalação

```bash
# Clone o projeto
git clone <seu-repositorio>
cd assistente-hubspot

# Ative o ambiente virtual
.venv\Scripts\activate  # Windows
# ou
source .venv/bin/activate  # Linux/Mac

# Instale as dependências
pip install -r requirements.txt
```

### 2. Configuração

```bash
# Copie o arquivo de exemplo
cp .env.example .env

# Configure sua URL do n8n
N8N_WEBHOOK_URL=http://localhost:5678/webhook/pergunta-hubspot
```

### 3. Executar

```bash
streamlit run app.py
```

Acesse: http://localhost:8501

## 📋 Estrutura do Projeto

```
assistente-hubspot/
├── app.py              # Aplicação principal
├── requirements.txt    # Dependências Python
├── .env               # Configurações (local)
├── .env.example       # Exemplo de configuração
├── Procfile           # Deploy Heroku
├── runtime.txt        # Versão Python
├── DEPLOY_GUIDE.md    # Guia completo de deploy
└── README.md          # Este arquivo
```

## 🔧 Configuração do n8n

### Dados enviados

```json
{
  "message": "Mensagem do usuário",
  "user_id": "ID único do usuário", 
  "timestamp": "2025-01-01T12:00:00Z",
  "source": "streamlit_chatbot"
}
```

### Resposta esperada

```json
{
  "output": "Sua resposta aqui"
}
```

ou formato de lista:

```json
[
  {
    "output": "Sua resposta aqui"
  }
]
```

## ✨ Funcionalidades

- Interface de chat limpa
- Integração com n8n via webhook
- Histórico de conversas na sessão
- Tratamento de erros
- Configuração via .env
- Deploy fácil para produção
