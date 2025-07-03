# 🤖 Assistente HubSpot

Assistente inteligente especializado em HubSpot, desenvolvido com Streamlit e integrado com n8n para automação de processos.

## ✨ Funcionalidades

- 💬 Interface de chat interativa
- 🎯 Especialista em HubSpot (CRM, Marketing, Vendas)
- ⚡ Respostas em tempo real via n8n
- 🌙 Tema escuro por padrão
- 📱 Design responsivo
- 🔄 Histórico de conversas na sessão

## 🛠️ Desenvolvimento Local

### Pré-requisitos

- Python 3.8+
- Git

### Instalação

```bash
# Clone o repositório
git clone <seu-repositorio>
cd assistente-hubspot

# Crie e ative o ambiente virtual
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

### Configuração

Crie um arquivo `.env` na raiz do projeto:

```env
N8N_WEBHOOK_URL=https://seu-n8n-endpoint/webhook/pergunta-hubspot
STREAMLIT_PORT=8501
```

### Executar

```bash
streamlit run app.py
```

A aplicação estará disponível em: http://localhost:8501

## 📋 Estrutura do Projeto

```
assistente-hubspot/
├── app.py                    # Aplicação principal Streamlit
├── requirements.txt          # Dependências Python
├── .env                     # Configurações locais (não commitado)
├── .streamlit/
│   ├── config.toml          # Configurações do Streamlit
│   └── secrets.toml         # Secrets para produção (não commitado)
├── .gitignore               # Arquivos ignorados pelo Git
└── README.md                # Este arquivo
```

## 🔧 Integração com n8n

### Dados enviados para o webhook

```json
{
  "message": "Mensagem do usuário",
  "user_id": "ID único do usuário", 
  "timestamp": "2025-07-03T12:00:00Z",
  "source": "streamlit_chatbot"
}
```

### Formato de resposta esperado

O n8n deve retornar uma das seguintes estruturas:

**Formato simples:**
```json
{
  "output": "Sua resposta aqui"
}
```

**Formato alternativo:**
```json
{
  "response": "Sua resposta aqui"
}
```

**Formato de lista:**
```json
[
  {
    "output": "Sua resposta aqui"
  }
]
```

## 🔍 Como Usar

1. **Inicie uma conversa:** Digite sua pergunta sobre HubSpot no campo de chat
2. **Aguarde a resposta:** O sistema processará via n8n e retornará a resposta
3. **Continue a conversa:** O histórico é mantido durante a sessão
4. **Explore tópicos:** Pergunte sobre CRM, automações, relatórios, integrações, etc.

## 💡 Exemplos de Perguntas

- "Como criar uma automação de lead scoring no HubSpot?"
- "Qual a diferença entre contatos e empresas no CRM?"
- "Como configurar um workflow de nutrição de leads?"
- "Como integrar HubSpot com outras ferramentas?"
- "Como criar relatórios personalizados no HubSpot?"

## 🚀 Tecnologias

- **Frontend:** Streamlit
- **Backend:** Python
- **Automação:** n8n
- **Comunicação:** HTTP webhooks
- **Estilo:** CSS customizado para tema escuro

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
