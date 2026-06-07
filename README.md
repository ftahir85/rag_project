# RAG Document Q&A Bot

A Retrieval Augmented Generation (RAG) system built from scratch in Python. Feed it a `.txt` document and ask questions about it in plain English — it answers strictly from your document, not from general AI knowledge.

Built as a learning project to understand how RAG works under the hood, without using any high-level frameworks like LangChain or LlamaIndex.

---

## Project Structure

```
rag_project/
├── ingest.py        # Load .txt file and split into chunks
├── embedder.py      # Embed chunks using sentence-transformers, store in FAISS
├── retriever.py     # Embed query, search FAISS, return top matching chunks
├── rag.py           # Main bot — retrieval + OpenAI = grounded answers
├── sample.txt       # Sample document used for testing
└── .gitignore       # Keeps .env, venv, and generated files out of GitHub
```

---

## Tech Stack

| Library | Purpose |
|---|---|
| `sentence-transformers` | Convert text to 384-dim vectors using all-MiniLM-L6-v2 |
| `faiss-cpu` | Store and search vectors by similarity |
| `openai` | GPT-4o-mini for answer generation |
| `python-dotenv` | Load API key securely from .env file |
| `numpy` | Vector array operations |

---

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/ftahir85/rag_project.git
cd rag_project
```

### 2. Create and activate virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install sentence-transformers faiss-cpu openai python-dotenv numpy
```

### 4. Add your OpenAI API key
Create a `.env` file in the project root:
```
OPENAI_API_KEY=your_key_here
```

---

## Usage

### Step 1 — Add your document
Place a `.txt` file in the project folder.

### Step 2 — Embed the document
```bash
python embedder.py
```
This creates `vector_store.index` and `chunks.pkl` — your local vector database. Run this once per document, or again whenever you change the document.

### Step 3 — Run the bot
```bash
python rag.py
```

### Step 4 — Ask questions
```
RAG Document Q&A Bot
Type 'quit' to exit

Your question: What are the benefits of reading?
Answer: Reading improves memory, analytical skills, and empathy...

Your question: What is deep reading?
Answer: Deep reading involves slow, thoughtful engagement with a text...

Your question: What is the capital of France?
Answer: I don't know based on the provided document.
```


