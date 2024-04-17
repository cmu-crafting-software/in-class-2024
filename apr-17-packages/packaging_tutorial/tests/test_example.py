from example_package_kferner import add_one

def test_answer():
    assert add_one(3) == 4

def test_answer_10():
    assert add_one(10) == 11
