from lib.greet import *

def test_greet_returns_name_greeting():
    result = greet("Benjamin")
    assert result == "Hello, Benjamin!"
