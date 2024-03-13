from wordle_parts import is_five_letters, is_yellow, is_red, is_green
from hypothesis import given, strategies as st

@given(st.text())
def test_is_five_letters_pbt(s: str) :
    assert is_five_letters(s) == (len(s) == 5)

@given(st.text(min_size=5, max_size=5),st.text(min_size=5, max_size=5), st.integers(min_value=0, max_value=4))
def test_is_yellow_pbt(guess: str, secret: str, pos: int) :
    if (is_green(guess, secret, pos)):
        assert is_yellow(guess,secret, pos) == False 
    elif (is_red(guess, secret, pos)):
        assert is_yellow(guess,secret, pos) == False
    else: 
        assert is_yellow (guess, secret,pos) == True

@given(st.text(min_size=5, max_size=5),st.text(min_size=5, max_size=5), st.integers(min_value=0, max_value=4))
def test_pbt(guess: str, secret: str, pos: int) :
    ## For a given letter alpha appearing m times in guess word exactly min (m,n) should be green or yellow where n is num tries aalpha appears in secret 
    alpha = guess[pos]
    n = secret.count(alpha)
    m = guess.count(alpha)
    assert min(m,n) == pos