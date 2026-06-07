from openai import OpenAI
from dotenv import load_dotenv
from retriever import retrieve
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask(query):
    results = retrieve(query, top_k=2)
    
    context = "\n\n".join([r["chunk"] for r in results])
    
    prompt = f"""You are a helpful assistant. Answer the question based only on the context provided below.
If the answer is not in the context, say "I don't know based on the provided document."

Context:
{context}

Question: {query}

Answer:"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    print("RAG Document Q&A Bot")
    print("Type 'quit' to exit\n")
    
    while True:
        query = input("Your question: ")
        if query.lower() == "quit":
            break
        answer = ask(query)
        print(f"\nAnswer: {answer}\n")
        print("-" * 50)