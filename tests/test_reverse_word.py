from src.reverse_word import *


def test_reverse_word_returns_og_string():
    """Tests revers_word returns og strng"""
    string = "This is a test"
    assert reverse_string(string) == "This is a test"
