import streamlit as st
import ollama
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

st.set_page_config(page_title = "RMTA", page_icon = ":100:", layout = "centered")

st.title("Agent 🌐")

st.caption("Agente de Perguntas e Respostas em Banco de Dados Jurídicos")

webpage_url = st.text_input("Digite a URL da webpage para criar o banco de dados:", type = "default")

if webpage_url:
    with st.spinner("Carregando a URL e criando o banco de dados..."):
        loader = WebBaseLoader(webpage_url)
        docs = loader.load()
        
        text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 50)
        splits = text_splitter.split_documents(docs)

        embeddings = OllamaEmbeddings(model = "llama3.2:1b")
        
        vectorstore = Chroma.from_documents(documents = splits, embedding = embeddings)

    st.success(f"URL {webpage_url} carregada com sucesso!")

    def ollama_llm(question, context):
        formatted_prompt = f"Question: {question}\n\nContext: {context}"
        
        response = ollama.chat(model = 'llama3.2:1b', messages = [{'role': 'user', 'content': formatted_prompt}])

        return response['message']['content']

    retriever = vectorstore.as_retriever()

    def combine_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    def rag_chain(question):
        retrieved_docs = retriever.invoke(question)
        
        formatted_context = combine_docs(retrieved_docs)
        
        return ollama_llm(question, formatted_context)

    prompt = st.text_input("Digite sua pergunta:")

    if prompt:
        with st.spinner("O Sistema de IA está consultando o banco de dados. Aguarde..."):
            result = rag_chain(prompt)
        
        st.write(result)