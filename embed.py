import chromadb
import sentence_transformers # type: ignore
from chunk import create_chunks

CHROMA_PATH = "chroma_db"
COLLECTION_NAME = "caldwell_unofficial_guide"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"


def build_vector_store():
    chunks = create_chunks()

    client = chromadb.PersistentClient(path=CHROMA_PATH)

    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass

    collection = client.create_collection(name=COLLECTION_NAME)

    model = sentence_transformers.SentenceTransformer(EMBEDDING_MODEL)
    texts = [chunk["text"] for chunk in chunks]
    embeddings = model.encode(texts).tolist()

    collection.add(
        ids=[chunk["id"] for chunk in chunks],
        documents=texts,
        embeddings=embeddings,
        metadatas=[
            {
                "source": chunk["source"],
                "chunk_index": chunk["chunk_index"]
            }
            for chunk in chunks
        ]
    )

    print(f"Stored {len(chunks)} chunks in ChromaDB.")
    print(f"Embedding model: {EMBEDDING_MODEL}")


if __name__ == "__main__":
    build_vector_store()