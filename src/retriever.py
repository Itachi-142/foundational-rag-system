import numpy as np

def cosine_similarity(vec1: list, vec2: list) -> float:
    v1 = np.array(vec1)
    v2 = np.array(vec2)

    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


def retrieve(query_embedding: list, vector_store, top_k: int = 3):
    scored_chunks = []

    for item in vector_store.store:
        score = cosine_similarity(query_embedding, item["embedding"])
        scored_chunks.append((score, item["text"]))

    # Higher score = more similar
    scored_chunks.sort(key=lambda x: x[0], reverse=True)

    return scored_chunks[:top_k]
