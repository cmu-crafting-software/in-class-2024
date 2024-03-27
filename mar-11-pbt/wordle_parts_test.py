from wordle_parts import is_five_letters, is_yellow
from hypothesis import given, strategies as st


#def test_is_five_letters_true() :
#    assert is_five_letters("tests")==True

#def test_is_five_letters_false() :
#    assert is_five_letters("test")==False


@given(st.text())
def test_is_five_letters_pbt(s: str):
    assert is_five_letters(s) == (len(s) == 5)
