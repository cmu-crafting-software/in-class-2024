from wordle_parts import is_five_letters, is_yellow, is_red, is_green
from hypothesis import given, strategies as st

@given(st.text())
def test_is_five_letters_pbt(s: str) :
    assert is_five_letters(s) == (len(s) == 5)

@given(st.text(min_size=5, max_size=5),st.text(min_size=5, max_size=5), st.integers(min_value=0, max_value=4))
def test_is_yellow_pbt(guess: str, secret: str, pos: int) :
    if(is_green(guess, secret, pos)):
        assert is_yellow(guess, secret, pos) == False
    elif(is_red(guess, secret, pos)):
        assert is_yellow(guess, secret, pos) == False
    else:
        assert is_yellow(guess, secret, pos) == True
@given(st.text(min_size=5, max_size=5),st.text(min_size=5, max_size=5), st.integers(min_value=0, max_value=4))
def test_is_yellow_pbt(guess: str, secret: str, pos: int) :
    alpha = guess[pos]
    # pass # TODO: Replace with your code

# @given(st.text(min_size=5, max_size=5),st.text(min_size=5, max_size=5), st.integers(min_value=0, max_value=4))
# def test_num_green_yellow(guess: str, secret: str, pos: int) :
#     letter = guess[pos]

#     num_in_guess = guess.count(letter)
#     num_in_secret = secret.count(letter)

#     # for n,m in zip(guess, secret):
#     #     if n == letter:
#     #         num_in_guess += 1
#     #     if m == letter:
#     #         num_in_secret += 1

#     count = 0
#     for index in range(5):
#         if is_yellow(guess, secret, index) or is_green(guess, secret, index):
#             count += 1
#         if is_green(guess, secret, index):
#             count += 1
#     assert count == min(num_in_guess, num_in_secret)

@given(st.text(min_size=5, max_size=5),st.text(min_size=5, max_size=5), st.integers(min_value=0, max_value=4))
def test_num_red_after_yellow(guess: str, secret: str, pos: int) :
    letter = guess[pos]
    got_first_red = False
    for index in range(5):
        if(guess[index] == letter):
            if(is_red(guess, secret, index)):
                got_first_red = True
            if(got_first_red and is_yellow(guess,secret,index)):
                assert False

@given(st.text(min_size=5, max_size=5),st.text(min_size=5, max_size=5), st.integers(min_value=0, max_value=4))
def test_is_green(guess: str, secret: str, pos: int) :
    letter = guess[pos]
    if (is_green(guess,secret, pos)):
        assert letter == secret[pos]
    if (letter == secret[pos]):
        assert is_green(guess, secret, pos)
