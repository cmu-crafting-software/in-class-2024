from wordle_parts import is_five_letters, is_yellow

def test_is_five_letters_true() :
    assert is_five_letters("tests")==True

def test_is_five_letters_false() :
    assert is_five_letters("test")==False

#“toils” “sunny” 4 true
def test_is_yellow_toils_sunny_0():
    assert is_yellow("toils","sunny",0)==False

# #eabcd abcde 0 true
def test_is_yellow_eabcd_abcde_0():
     assert is_yellow("eabcd","xxxxe",0) == True

# #solid “sunny” 0 false
def test_is_yellow_solid_sunny_0():
    assert is_yellow("solid","sunny",0) == False

#solid “sunny” 1 false
def test_is_yellow_solid_sunny_1():
    assert is_yellow("solid","sunny",1) == False

#eeabc eabce 1 true
def test_is_yellow_eeabc_eabce_1():
    assert is_yellow("eeabc","eabce",1) == True

#eeabc eabcd 1 false
def test_is_yellow_eeabc_eabcd_1():
    assert is_yellow("eeabc","eabcd",1) == False

# #eeabc eabcd 1 false
def test_is_yellow_eeabc_eabcd_0():
    assert is_yellow("eeabc","eabcd",0) == False

# #eeabc eabce 0 false
def test_is_yellow_eeabc_eabce_0():
    assert is_yellow("eeabc","eabcd",0) == False

# eeeee aaaee 1 true
def test_is_yellow_eeeee_aaaee_1():
    assert is_yellow("eeeee","aaaee",1) == True

# eeeee aaaee 2 false
def test_is_yellow_eeeee_aaaee_2():
    assert is_yellow("eeeee","eeeaa",2) == False
