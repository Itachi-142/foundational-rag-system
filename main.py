from src.source_loader import load_document
from src.chunker import chunk_text
from src.embedder import embed_text
from src.vector_store import VectorStore
from src.retriever import retrieve
from src.llm import generate_answer

def main():
    text = load_document("data/best_dsa_notes.pdf")
    chunks = chunk_text(text)

    store = VectorStore()
    for chunk in chunks:
        store.add(embed_text(chunk), chunk)

    question = input("Ask a question: ")
    query_embedding = embed_text(question)

    results = retrieve(query_embedding, store)

    # Combine retrieved chunks
    context = "\n\n".join([chunk for _, chunk in results])

    answer = generate_answer(context, question)

    print("\n🤖 Answer:\n")
    print(answer)

if __name__ == "__main__":
    main()
