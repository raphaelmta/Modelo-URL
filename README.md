🧠 RMTA – Agente Jurídico com RAG e LLM
Este projeto implementa um Agente de Perguntas e Respostas que utiliza técnicas de RAG (Retrieval-Augmented Generation) com modelos LLM e dados extraídos de páginas web jurídicas. A interface é construída com Streamlit, e o agente utiliza Ollama para processamento local do modelo de linguagem.

🚀 Funcionalidades
Extração de conteúdo jurídico diretamente de uma URL fornecida.

Criação de um banco vetorial com embeddings do modelo llama3.2:1b.

Sistema de recuperação de contexto relevante e geração de resposta com LLM.

Interface amigável via navegador.

🛠️ Tecnologias Utilizadas
Streamlit

LangChain

Ollama – modelo llama3.2:1b

ChromaDB – armazenamento vetorial

🧩 Estrutura de Funcionamento
Input da URL: O usuário insere uma URL jurídica.

Carregamento e Split: O conteúdo da página é dividido em chunks.

Geração de Embeddings: Usando o modelo Ollama local.

Armazenamento Vetorial: Criação do banco de dados em Chroma.

Pergunta e Resposta: A pergunta do usuário é respondida com base no conteúdo vetorial mais relevante.

📌 Requisitos
Python 3.8+

Ollama instalado e com o modelo llama3.2:1b baixado localmente.

Internet para acessar e carregar o conteúdo das URLs.

🧪 Exemplo de Uso
Insira uma URL jurídica (como um artigo de lei ou regulamento).

Digite uma pergunta sobre o conteúdo daquela URL.

O sistema responde com base no conteúdo recuperado.
