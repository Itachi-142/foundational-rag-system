import ollama

def generate_answer(context: str, question: str) -> str:
    prompt = f"""
You are a knowledgeable teaching assistant.

Rules:
- Use ONLY the provided context.
- If the answer is not clearly present, say: "I don't know based on the document."
- Keep the answer clear and concise.
- Use simple language.

Context:
{context}

Question:
{question}

Answer (3-5 lines max):
"""

    response = ollama.chat(
        model="phi3:latest",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]
