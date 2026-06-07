from PyPDF2 import PdfReader

def load_text(filepath):
    if filepath.endswith(".pdf"):
        reader = PdfReader(filepath)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    else:
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
    return text

def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

if __name__ == "__main__":
    text = load_text("sample.txt")
    chunks = chunk_text(text)
    print(f"Total characters: {len(text)}")
    print(f"Total chunks: {len(chunks)}")
    print(f"\nFirst chunk preview:\n{chunks[0]}")