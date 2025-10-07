def find_anomalous_words(text: str) -> list[str]:
    """
    Находит слова, длина которых отличается от средней длины слов в тексте более чем на 2 символа.



    :param text: Входная строка.
    :return: Список аномальных слов.
    """
    if not text.strip():
        return []
    cleaned_words = []
    for word in text.split():
        cleaned = "".join(ch for ch in word if ch.isalnum())
        if cleaned:
            cleaned_words.append(cleaned)
    if not cleaned_words:
        return []
    avg_len: float = sum(len(word) for word in cleaned_words) / len(cleaned_words)
    result: list[str] = [
        word for word in cleaned_words if abs(len(word) - avg_len) >= 2
    ]
    return result
