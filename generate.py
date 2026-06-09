import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
LLM_MODEL = os.getenv("LLM_MODEL", "llama-3.3-70b-versatile")

client = Groq(api_key=GROQ_API_KEY)


SYSTEM_PROMPT = """
You are an assistant for The Unofficial Guide to CS Professors and CS Courses at Caldwell University.

Answer the user's question using ONLY the retrieved context.
Do not use outside knowledge.
If the retrieved context does not contain enough information to answer, say:
"I don't have enough information in the collected documents to answer that."

Every answer must be grounded in the retrieved context.
Keep the answer concise.
Mention the source document names when explaining the answer.
"""


def format_context(retrieved_chunks):
    context_parts = []

    for chunk in retrieved_chunks:
        context_parts.append(
            f"[Source: {chunk['source']}, Chunk: {chunk['chunk_index']}]\n"
            f"{chunk['text']}"
        )

    return "\n\n".join(context_parts)


def generate_response(query, retrieved_chunks):
    if not GROQ_API_KEY:
        raise ValueError("Missing GROQ_API_KEY. Add it to your .env file.")

    context = format_context(retrieved_chunks)

    user_prompt = f"""
Retrieved context:
{context}

User question:
{query}

Answer using only the retrieved context.
"""

    completion = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.2,
    )

    answer = completion.choices[0].message.content

    sources = []
    for chunk in retrieved_chunks:
        source_label = f"{chunk['source']} chunk {chunk['chunk_index']}"
        if source_label not in sources:
            sources.append(source_label)

    return {
        "answer": answer,
        "sources": sources,
    }


if __name__ == "__main__":
    from retrieve import retrieve

    question = "Which professor gives good feedback?"
    chunks = retrieve(question)
    result = generate_response(question, chunks)

    print("ANSWER:")
    print(result["answer"])
    print("\nSOURCES:")
    for source in result["sources"]:
        print("-", source)