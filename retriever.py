import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def load_store():
    index = faiss.read_index("vector_store.index")
    with open("chunks.pkl", "rb") as f:
        chunks = pickle.load(f)
    return index, chunks

def retrieve(query, top_k=2):
    index, chunks = load_store()

    query_vector = model.encode([query])
    query_vector = np.array(query_vector).astype("float32")

    distances, indices = index.search(query_vector, top_k)

    results = []
    for i, idx in enumerate(indices[0]):
        results.append({
            "chunk": chunks[idx],
            "distance": distances[0][i]
        })
    return results

if __name__ == "__main__":
    query = "What are the benefits of reading?"
    results = retrieve(query)
    print(f"Query: {query}\n")
    for i, r in enumerate(results):
        print(f"--- Result {i+1} (distance: {r['distance']:.4f}) ---")
        print(r["chunk"])
        print()