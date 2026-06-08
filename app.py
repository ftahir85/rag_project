import streamlit as st
import os
from dotenv import load_dotenv
from embedder import embed_and_store
from rag import ask

load_dotenv()

st.set_page_config(page_title="RAG Q&A Bot", page_icon="🤖", layout="centered")

st.title("🤖 RAG Document Q&A Bot")
st.caption("Upload a .txt file, then ask questions about it.")

# --- Sidebar ---
with st.sidebar:
    st.header("📄 Upload Document")
    uploaded_file = st.file_uploader("Choose a .txt file", type=["txt"])

    if uploaded_file:
        with open("sample.txt", "wb") as f:
            f.write(uploaded_file.read())
        with st.spinner("Embedding document..."):
            embed_and_store("sample.txt")
        st.success(f"✅ '{uploaded_file.name}' embedded successfully!")

    st.divider()
    st.markdown("**How it works**")
    st.markdown("1. Upload a `.txt` file")
    st.markdown("2. Ask questions about it")
    st.markdown("3. Answers come from your document only")

# --- Chat ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask a question about your document..."):
    if not os.path.exists("vector_store.index"):
        st.warning("Please upload a document first using the sidebar.")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                answer = ask(prompt)
            st.markdown(answer)

        st.session_state.messages.append({"role": "assistant", "content": answer})