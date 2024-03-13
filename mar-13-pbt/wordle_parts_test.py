from wordle_parts import is_five_letters, is_yellow, is_red, is_green
from hypothesis import given, strategies as st

@given(st.text())
def test_is_five_letters_pbt(s: str) :
    assert is_five_letters(s) == (len(s) == 5)

@given(st.text(min_size=5, max_size=5),st.text(min_size=5, max_size=5), st.integers(min_value=0, max_value=4))
def test_is_yellow_pbt(guess: str, secret: str, pos: int) :
    if(is_green(guess,secret,pos)):
        assert is_yellow(guess,secret,pos) == False
    elif(is_red(guess,secret,pos)):
        assert is_yellow(guess,secret,pos) == False
    else:
        assert is_yellow(guess,secret,pos) == True

@given(st.text(min_size=5, max_size=5),st.text(min_size=5, max_size=5), st.integers(min_value=0, max_value=4))
def test_is_color_correct_pbt(guess: str, secret: str, pos: int) :
    alpha = guess[pos] 
    count_m = 0
    count_n = 0
    for i in guess:
        if i == alpha :
            count_m = count_m + 1
        else: count_m = count_m 
    for i in secret:
        if i == alpha :
            count_n = count_n + 1
        else: count_n = count_n
    assert count_m <= min(count_m, count_n)