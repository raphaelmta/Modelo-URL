
# 🧠 RMTA – Agente Jurídico com RAG e LLM

Este projeto implementa um **Agente de Perguntas e Respostas** que utiliza técnicas de **RAG (Retrieval-Augmented Generation)** com modelos **LLM** e dados extraídos de **páginas web jurídicas**.  
A interface é construída com **Streamlit**, e o agente utiliza **Ollama** para o processamento local do modelo de linguagem.

---

## 🚀 Funcionalidades

- Extração de conteúdo jurídico diretamente de uma URL fornecida.  
- Criação de um banco vetorial com embeddings do modelo `llama3.2:1b`.  
- Sistema de recuperação de contexto relevante e geração de resposta com LLM.  
- Interface amigável e interativa via navegador.

---

## 🛠️ Tecnologias Utilizadas

- **Streamlit**  
- **LangChain**  
- **Ollama** – modelo `llama3.2:1b`  
- **ChromaDB** – armazenamento vetorial

---

## 🧩 Estrutura de Funcionamento

1. **Input da URL**: o usuário insere uma URL jurídica.  
2. **Carregamento e Split**: o conteúdo da página é dividido em pedaços (chunks).  
3. **Geração de Embeddings**: os textos são transformados em vetores com o modelo Ollama.  
4. **Armazenamento Vetorial**: os vetores são armazenados no ChromaDB.  
5. **Pergunta e Resposta**: a pergunta do usuário é respondida com base no conteúdo mais relevante do banco vetorial.

---

## 📌 Requisitos

- Python 3.8 ou superior  
- Ollama instalado localmente com o modelo `llama3.2:1b`  
- Conexão com a internet para carregar o conteúdo das URLs

---

## 🧪 Exemplo de Uso

1. Insira uma **URL jurídica** (ex.: artigo de lei ou norma).  
2. Digite uma **pergunta** sobre o conteúdo daquela URL.  
3. O sistema irá **responder automaticamente**, com base nas informações recuperadas da página.
