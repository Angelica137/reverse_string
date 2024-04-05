from src.reverse_word import reverse_string


def test_reverse_word_returns_reversed_wrods_as_req_short_words():
    """Tests revers_word returns given string when there
        are no long words"""
    string = "This is a test"
    assert reverse_string(string) == "This is a test"


def test_reverse_word_returns_reversed_wrods_as_req_long_words():
    """Tests revers_word returns a string with reversed words if long"""
    string = "Hey fellow warriors"
    assert reverse_string(string) == "Hey wollef sroirraw"
