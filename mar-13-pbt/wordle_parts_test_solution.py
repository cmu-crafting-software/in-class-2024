from wordle_parts import is_five_letters, is_yellow, is_red, is_green
from hypothesis import given, strategies as st

@given(st.text())
def test_is_five_letters_pbt(s: str) :
    assert is_five_letters(s) == (len(s) == 5)

@given(st.text(min_size=5, max_size=5),st.text(min_size=5, max_size=5), st.integers(min_value=0, max_value=4))
def test_is_yellow_pbt(guess: str, secret: str, pos: int) :
    # Yellow should only return True if is_red and is_green are both False
    # Yellow should only return False if is_red or is_green is True
    if(is_yellow(guess, secret, pos)):
        assert not is_red(guess, secret, pos)
        assert not is_green(guess, secret, pos)
    else:
        assert is_red(guess, secret, pos) or is_green(guess, secret, pos)