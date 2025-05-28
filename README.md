# 🤖 Mr.HelpMate — Retrieval-Augmented QA System


**Mr.HelpMate** is a flexible and user-friendly **Retrieval-Augmented Generation (RAG)** application that allows users to upload PDF documents, semantically index their content, and ask natural language questions. It retrieves, re-ranks, and generates intelligent responses by leveraging the power of modern NLP techniques.


## 🚀 Features


The assistant helps you **answer your queries** by providing:

### 📤 1. Upload PDF and Create Vector Store
- Upload any PDF document (manuals, reports, policies, etc.).
- Extracts raw text using pdfplumber.
- Chunks and embeds text using Sentence Transformers.
- Stores embeddings in a ChromaDB vector store for semantic search.

### 🔍 2. Query the System
- Ask natural language questions.
- Retrieves the most relevant chunks from the document based on semantic similarity.

### 🧠 3. Generated Output
- Outputs an intelligent answer based on retrieved content.

### 📑 4. Retrieved & Re-ranked Documents with Scores
- Uses cross-encoder models to re-rank top retrieved chunks.
- Displays a table view with document IDs, scores, and content for transparency.

## 🧰 Tech Stack
- Streamlit — Interactive web UI
- pdfplumber — PDF text extraction
- Sentence Transformers — Embedding generation & Re-ranking models
- ChromaDB — Vector database


## 💼 Use Cases
### 📚 Academic paper analysis
### 🏛️ Legal document question answering
### 🏢 Internal knowledge base search
### 📄 Policy and manual understanding
### 🛠️ Technical documentation support


## 🚀 Running the App

### 🔹 Option 1: Run Locally with CLI

1. Make sure Python 3.10+ and pip are installed.
2. Create a virtualenv
   ```bash
   python -m venv .venv
3. Activate the virtualenv
   ```bash
   source venv/bin/activate

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
5. Create a .env file.
6. Add your OPENAI_API_KEY in the .env
7. Run the Streamlit app:
   ```bash
   streamlit run main.py
8. Open the Smart Travel Bot UI in browser
   ```bash
   http://localhost:8501/

### 🔹 Option 2: Run Locally with Docker
1. Make sure docker is installed and is updated.
2. Change the directory to shubham_sharma_help_mate_ai
   ```bash
   cd shubham_sharma_help_mate_ai
3. Build the docker image
   ```bash
   docker build -t help_mate:latest .
4. Run the container
   ```bash
   docker run -p 8501:8501 -e OPENAI_API_KEY=<YOUR_OPENAI_API_KEY> -d --name assitant help_mate:latest
5. To check the logs run the below command
   ```bash
   docker logs -f assitant
6. Open the Smart Travel Bot UI in browser
   ```bash
   http://localhost:8501/


## 👤 Author
**Shubham Sharma**
