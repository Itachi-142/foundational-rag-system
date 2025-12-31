from sentence_transformers import SentenceTransformer

# Load model once (important)
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(text: str) -> list:
    """
    Converts text into a real semantic embedding.
    """
    embedding = model.encode(text)
    return embedding.tolist()
