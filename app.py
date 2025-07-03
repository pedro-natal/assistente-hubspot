import streamlit as st
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

# Carrega variáveis de ambiente
load_dotenv()


class N8nChatbot:
    def __init__(self):
        self.webhook_url = os.getenv("N8N_WEBHOOK_URL")

    def send_message_to_n8n(self, message, user_id=None):
        """Envia mensagem para o webhook do n8n"""
        try:
            payload = {
                "message": message,
                "user_id": user_id or st.session_state.get("user_id", "anonymous"),
                "timestamp": datetime.now().isoformat(),
                "source": "streamlit_chatbot",
            }

            response = requests.post(self.webhook_url, json=payload, timeout=30)

            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            st.error(f"Erro ao conectar com n8n: {str(e)}")
            return None
        except Exception as e:
            st.error(f"Erro inesperado: {str(e)}")
            return None

    def extract_n8n_response(self, response):
        """Extrai a resposta do n8n"""
        try:
            # Lista com objetos: [{"output": "texto"}]
            if isinstance(response, list) and len(response) > 0:
                first_item = response[0]
                if isinstance(first_item, dict):
                    return (
                        first_item.get("output")
                        or first_item.get("response")
                        or first_item.get("message")
                        or str(first_item)
                    )

            # Objeto direto: {"output": "texto"}
            elif isinstance(response, dict):
                return (
                    response.get("output")
                    or response.get("response")
                    or response.get("message")
                    or str(response)
                )

            # String direta
            elif isinstance(response, str):
                return response

            return str(response)

        except Exception as e:
            st.error(f"Erro ao processar resposta: {str(e)}")
            return "Erro ao processar resposta"


def initialize_session_state():
    """Inicializa o estado da sessão"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
        # Adiciona mensagem de boas-vindas automática
        welcome_message = "👋 Olá dev, bem-vindo ao Assistente HubSpot!\n\nSou seu assistente especializado em HubSpot."
        st.session_state.messages.append(
            {"role": "assistant", "content": welcome_message}
        )

    if "user_id" not in st.session_state:
        st.session_state.user_id = f"user_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    if "chatbot" not in st.session_state:
        st.session_state.chatbot = N8nChatbot()


def display_chat_messages():
    """Exibe as mensagens do chat"""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


def main():
    st.set_page_config(
        page_title="Assistente HubSpot", page_icon="🤖", layout="centered"
    )

    initialize_session_state()

    st.title("🤖 Assistente HubSpot")

    # Verificar se webhook está configurado
    if not st.session_state.chatbot.webhook_url:
        st.error("⚠️ Webhook não configurado! Configure N8N_WEBHOOK_URL no arquivo .env")
        st.stop()

    # Exibe mensagens do histórico
    display_chat_messages()

    # Input para nova mensagem
    if prompt := st.chat_input("Digite sua mensagem..."):
        # Adiciona mensagem do usuário
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Exibe mensagem do usuário
        with st.chat_message("user"):
            st.markdown(prompt)

        # Processa mensagem com n8n
        with st.chat_message("assistant"):
            with st.spinner("Processando..."):
                response = st.session_state.chatbot.send_message_to_n8n(prompt)

            if response:
                bot_response = st.session_state.chatbot.extract_n8n_response(response)
                st.markdown(bot_response)
                st.session_state.messages.append(
                    {"role": "assistant", "content": bot_response}
                )
            else:
                error_msg = "Não foi possível obter resposta. Tente novamente."
                st.error(error_msg)
                st.session_state.messages.append(
                    {"role": "assistant", "content": error_msg}
                )

        st.rerun()


if __name__ == "__main__":
    main()
