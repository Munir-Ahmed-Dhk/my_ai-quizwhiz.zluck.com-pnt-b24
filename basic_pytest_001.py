import math

def test_negative_sqrt():
    num = -9
    try:
        math.sqrt(num)
        assert False, "Expected ValueError for negative input"
    except ValueError:
        pass  # Test passes if ValueError is raised

def test_multiplication():
    a = 4
    b = 5
    assert a * b == 20

def test_string_equality():
    str1 = "Hello"
    str2 = "Hello"
    assert str1 == str2