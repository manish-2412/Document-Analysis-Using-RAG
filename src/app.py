import streamlit as st
from vectorstore import VectorStore
from chatbot import Chatbot
import uuid

def main():
    st.title("Document Analysis using RAG")
    st.write("Upload a PDF, input your API keys, and ask questions")

    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    with st.sidebar:
        st.header("API Keys")
        cohere_api_key = st.text_input("Cohere API Key", type="password")
        pinecone_api_key = st.text_input("Pinecone API Key", type="password")

    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    user_query = st.text_input("Ask a question based on the document")

    if st.button("Submit") and uploaded_file and cohere_api_key and pinecone_api_key:
        with st.spinner("Processing PDF..."):
            with open("uploaded_document.pdf", "wb") as f:
                f.write(uploaded_file.read())

            vectorstore = VectorStore("uploaded_document.pdf", cohere_api_key, pinecone_api_key)
            chatbot = Chatbot(vectorstore, cohere_api_key)

            with st.spinner("Generating response..."):
                response, retrieved_docs = chatbot.respond(user_query)
                st.session_state["chat_history"].append((user_query, response, retrieved_docs))

    if st.session_state["chat_history"]:
        for user_query, response, retrieved_docs in st.session_state["chat_history"]:
            st.write(f"**You:** {user_query}")

            accumulated_response = ""
            for event in response:
                if event.event_type == "text-generation":
                    accumulated_response += event.text
            st.write(f"**Bot:** {accumulated_response}")

    st.markdown("---")
    st.markdown("<p style='text-align: center; color: gray;'>Created by Manish Chandrasekar</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()