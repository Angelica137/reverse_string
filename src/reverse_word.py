def reverse_string(sentence) -> str:
    words = sentence.split(" ")
    new_sentence = ""
    for word in words:
        if len(word) < 5:
            new_sentence += word + " "
        else:
            reverse_word = word[::-1]
            new_sentence += reverse_word + " "
    return new_sentence.rstrip()
