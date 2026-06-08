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
├── rag.py           # Core RAG logic — retrieval + OpenAI generation
├── app.py           # Streamlit chat UI
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
| `streamlit` | Chat web UI |

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
pip install sentence-transformers faiss-cpu openai python-dotenv numpy streamlit
```

### 4. Add your OpenAI API key
Create a `.env` file in the project root:
```
OPENAI_API_KEY=your_key_here
```

---

## Usage

### Option 1 — Chat UI (Streamlit)

```bash
streamlit run app.py
```

Opens in your browser at `http://localhost:8501`

1. Upload your `.txt` file using the sidebar
2. Wait for "✅ embedded successfully!"
3. Type your question in the chat box
4. Get answers grounded in your document

### Option 2 — Terminal

```bash
python embedder.py
python rag.py
```

```
RAG Document Q&A Bot
Type 'quit' to exit

Your question: What are the benefits of reading?
Answer: Reading improves memory, analytical skills, and empathy...

Your question: What is the capital of France?
Answer: I don't know based on the provided document.
```

---



---

*Python 3.14 — Windows 11*
