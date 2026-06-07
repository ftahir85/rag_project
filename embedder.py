import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer
from ingest import load_text, chunk_text

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_and_store(filepath):
    text = load_text(filepath)
    chunks = chunk_text(text)

    print(f"Embedding {len(chunks)} chunks...")
    embeddings = model.encode(chunks, show_progress_bar=True)
    embeddings = np.array(embeddings).astype("float32")

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    faiss.write_index(index, "vector_store.index")

    with open("chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

    print(f"Done! Stored {index.ntotal} vectors.")
    print(f"Embedding dimension: {dimension}")

if __name__ == "__main__":
    embed_and_store("sample.txt")