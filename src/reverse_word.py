def reverse_string(sentence: str) -> str:
    words = [word[::-1] if len(word) >= 5 else word for word in sentence.split(" ")]
    new_sentence = " ".join(words)
    return new_sentence
