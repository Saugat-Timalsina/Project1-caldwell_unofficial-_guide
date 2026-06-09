import chromadb
from sentence_transformers import SentenceTransformer

CHROMA_PATH = "chroma_db"
COLLECTION_NAME = "caldwell_unofficial_guide"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"


def retrieve(query: str, top_k: int = 4):
    client = chromadb.PersistentClient(path=CHROMA_PATH)
    collection = client.get_collection(name=COLLECTION_NAME)

    model = SentenceTransformer(EMBEDDING_MODEL)
    query_embedding = model.encode([query]).tolist()[0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    retrieved = []

    for i in range(len(results["documents"][0])):
        retrieved.append({
            "text": results["documents"][0][i],
            "source": results["metadatas"][0][i]["source"],
            "chunk_index": results["metadatas"][0][i]["chunk_index"],
            "distance": results["distances"][0][i]
        })

    return retrieved


if __name__ == "__main__":
    test_queries = [
        "Which professor gives good feedback?",
        "Which professor seems difficult?",
        "What CS courses does Caldwell offer?"
    ]

    for query in test_queries:
        print("\n" + "=" * 80)
        print(f"QUERY: {query}")
        results = retrieve(query)

        for r in results:
            print("-" * 80)
            print(f"Source: {r['source']} | Chunk: {r['chunk_index']} | Distance: {r['distance']:.4f}")
            print(r["text"][:500])