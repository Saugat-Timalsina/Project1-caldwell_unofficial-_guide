from retrieve import retrieve
from generate import generate_response


def ask(question: str):
    retrieved_chunks = retrieve(question, top_k=4)
    result = generate_response(question, retrieved_chunks)

    return {
        "question": question,
        "answer": result["answer"],
        "sources": result["sources"],
        "retrieved_chunks": retrieved_chunks,
    }


if __name__ == "__main__":
    question = input("Ask a question: ")
    result = ask(question)

    print("\nAnswer:")
    print(result["answer"])

    print("\nSources:")
    for source in result["sources"]:
        print(f"- {source}")