from pathlib import Path
import re

RAW_DIR = Path("data/raw")


def clean_text(text: str) -> str:
    text = text.replace("\r\n", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


def load_documents(raw_dir: Path = RAW_DIR):
    documents = []

    for path in sorted(raw_dir.glob("*.txt")):
        text = path.read_text(encoding="utf-8")
        cleaned = clean_text(text)

        if cleaned:
            documents.append({
                "source": path.name,
                "text": cleaned
            })

    return documents


if __name__ == "__main__":
    docs = load_documents()
    print(f"Loaded {len(docs)} documents.")
    for doc in docs:
        print(f"- {doc['source']}: {len(doc['text'])} characters")