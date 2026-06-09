from ingest import load_documents

CHUNK_SIZE = 700
OVERLAP = 100


def chunk_text(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = OVERLAP):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


def create_chunks():
    documents = load_documents()
    all_chunks = []

    for doc in documents:
        chunks = chunk_text(doc["text"])

        for i, chunk in enumerate(chunks):
            all_chunks.append({
                "id": f"{doc['source']}_chunk_{i}",
                "source": doc["source"],
                "chunk_index": i,
                "text": chunk
            })

    return all_chunks


if __name__ == "__main__":
    chunks = create_chunks()
    print(f"Created {len(chunks)} chunks.\n")

    for chunk in chunks[:5]:
        print("=" * 80)
        print(f"ID: {chunk['id']}")
        print(f"Source: {chunk['source']}")
        print(chunk["text"])
        print()