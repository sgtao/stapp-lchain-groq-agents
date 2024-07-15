import os

from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema import ChatMessage

# from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import streamlit as st


class StreamHandler(BaseCallbackHandler):
    def __init__(self, container, initial_text=""):
        self.container = container
        self.text = initial_text

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.text += token
        self.container.markdown(self.text)


# Run the chat application
st.set_page_config(page_title="basic streaming", page_icon="🌊")
st.subheader("🌊: basic streaming using ChatGroq")

if "groq_api_key" in st.session_state:
    groq_api_key = st.session_state.groq_api_key
elif os.getenv("GROQ_API_KEY"):
    st.session_state.groq_api_key = os.getenv("GROQ_API_KEY")
    groq_api_key = st.session_state.groq_api_key
else:
    groq_api_key = ""

with st.sidebar:
    # API-KEYの設定
    st.session_state.groq_api_key = st.text_input(
        "Groq API Key",
        key="api_key",
        type="password",
        placeholder="gsk_...",
        value=groq_api_key,
    )
    groq_api_key = st.session_state.groq_api_key
    "[Get an Groq API key](https://console.groq.com/keys)"


if "messages" not in st.session_state:
    st.session_state["messages"] = [
        ChatMessage(role="assistant", content="How can I help you?")
    ]

for msg in st.session_state.messages:
    st.chat_message(msg.role).write(msg.content)

if prompt := st.chat_input():
    st.session_state.messages.append(ChatMessage(role="user", content=prompt))
    st.chat_message("user").write(prompt)

    if not st.session_state.groq_api_key:
        st.info("Please add your Groq API key to continue.")
        st.stop()

    with st.chat_message("assistant"):
        stream_handler = StreamHandler(st.empty())
        # llm = ChatOpenAI(
        #     openai_api_key=openai_api_key,
        #     streaming=True,
        #     callbacks=[stream_handler],
        # )
        try:
            llm = ChatGroq(
                temperature=0,
                model="llama3-70b-8192",
                api_key=st.session_state.groq_api_key,
                callbacks=[stream_handler],  # StreamHandlerをcallbacksに追加
            )
            response = llm.invoke(st.session_state.messages)
            # print(response)
            completion_content = response.content
            st.session_state.messages.append(
                ChatMessage(role="assistant", content=completion_content)
            )
            st.write(completion_content)
        except Exception as e:
            st.error(f"エラーが発生しました: {str(e)}")
