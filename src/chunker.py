import re

def chunk_text(text: str, max_words: int = 200) -> list:
    """
    Splits text into chunks based on sentences while respecting max size.
    """
    sentences = re.split(r'(?<=[.!?])\s+', text)

    chunks = []
    current_chunk = []
    current_length = 0

    for sentence in sentences:
        words = sentence.split()
        word_count = len(words)

        if current_length + word_count <= max_words:
            current_chunk.append(sentence)
            current_length += word_count
        else:
            chunks.append(" ".join(current_chunk))
            current_chunk = [sentence]
            current_length = word_count

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks
