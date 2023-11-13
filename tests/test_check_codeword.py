from lib.check_codeword import *

def test_check_codeword_for_correct_word():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_check_codeword_for_close_word():
    result = check_codeword("hooooorse")
    assert result == "Close, but nope."

def test_check_codeword_for_incorrect_word():
    result = check_codeword("burrito")
    assert result == "WRONG!"
