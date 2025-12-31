class VectorStore:
    def __init__(self):
        self.store = []

    def add(self, embedding: list, text: str):
        """
        Stores embedding with its corresponding text chunk.
        """
        self.store.append({
            "embedding": embedding,
            "text": text
        })

    def size(self) -> int:
        return len(self.store)

    def preview(self, n: int = 3):
        """
        Preview first n stored items.
        """
        return self.store[:n]
