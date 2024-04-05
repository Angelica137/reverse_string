from src.reverse_word import reverse_string


def test_reverse_word_returns_list_of_words():
    """Tests revers_word returns list of words
        in the og string"""
    string = "This is a test"
    assert reverse_string(string) == ["This", "is", "a", "test"]
