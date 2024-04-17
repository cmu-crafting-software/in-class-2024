from wordle_parts import * 
from hypothesis import given, strategies as st

@given(st.text())
def test_is_five_letters_pbt(s: str) :
    assert is_five_letters(s) == (len(s) == 5)

@given(st.text(min_size=5, max_size=5),st.text(min_size=5, max_size=5), st.integers(min_value=0, max_value=4))
def test_is_yellow_pbt(guess: str, secret: str, pos: int) :
    pass # TODO: Replace with your code