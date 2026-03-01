# 📚 PDF Assistant AI – RAG v0.0.1

An intelligent PDF Question-Answering system using **Retrieval-Augmented Generation (RAG)** powered by:

* 🐍 Python
* 🚀 FastAPI
* 🧠 SentenceTransformers
* 📦 FAISS (Vector Database)
* 🦙 Ollama (LLM - Llama3)
* 📄 PDF document processing

---

# 🎯 Project Overview

This project implements a **local RAG (Retrieval-Augmented Generation)** pipeline that allows users to:

* Upload or process a PDF document
* Ask natural language questions
* Receive answers grounded in the document content

The system avoids hallucination by retrieving relevant document chunks before generating responses.

---

# 🧠 How It Works

```
PDF → Text Extraction → Chunking
     → Embeddings → FAISS Index
     → User Question
     → Similarity Search
     → Context Injection
     → LLM (Ollama)
     → Final Answer
```

---

# 🏗 Architecture

## Components

| Component           | Role                     |
| ------------------- | ------------------------ |
| PDF Loader          | Extract text             |
| Text Splitter       | Chunking                 |
| SentenceTransformer | Create embeddings        |
| FAISS               | Vector similarity search |
| Ollama (Llama3)     | Text generation          |
| FastAPI             | REST API                 |

---

# 📂 Project Structure

```
rag_v0/
│
├── app.py
├── pdf_loader.py
├── vector_store.py
├── ollama_client.py
├── .env
├── data/
│     └── sample.pdf
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone repository

```
git clone <your_repo_url>
cd rag_v0
```

---

## 2️⃣ Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

## 3️⃣ Install dependencies

```
pip install fastapi uvicorn langchain faiss-cpu pypdf sentence-transformers python-dotenv requests
```

---

## 4️⃣ Install Ollama

Download from:

[https://ollama.com](https://ollama.com)

Pull model:

```
ollama pull llama3
```

Test:

```
ollama run llama3
```

---

# 🔐 Environment Variables

Create `.env` file:

```
MODEL_NAME=llama3
OLLAMA_URL=http://localhost:11434
TOP_K=3
```

---

# 🚀 Run the Application

```
uvicorn app:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

# 📬 API Usage

### Endpoint

```
POST /ask
```

### Request Body

```json
{
  "question": "What is this document about?"
}
```

### Response

```json
{
  "answer": "The document discusses..."
}
```

---

# 🧮 Technical Details

## Embedding Model

`sentence-transformers/all-MiniLM-L6-v2`

## Vector Search

FAISS L2 distance

## LLM

Llama3 via Ollama local API

---

# 🔥 Features

* Local LLM (no OpenAI API required)
* Semantic search
* Context-aware answering
* Clean API architecture
* Environment-based configuration

---

# 🚀 Future Improvements (v0.0.2)

* PDF upload via API
* Persistent FAISS index
* Streaming responses
* Conversation memory
* Multi-document support
* Docker deployment

---

# 🎓 Academic Relevance

This project demonstrates:

* NLP
* Vector databases
* Deep Learning embeddings
* Large Language Models
* Modern AI system architecture
* Retrieval-Augmented Generation

Suitable for:

* Master thesis
* AI engineering portfolio
* Data Science projects

---

# 🏆 Author

Abdellatif Oumansour
Master Student – Artificial Intelligence

---

# 📜 License

MIT License




