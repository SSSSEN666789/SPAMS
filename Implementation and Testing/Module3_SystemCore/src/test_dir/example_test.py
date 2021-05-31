from .example import Example

def test_test():
    assert True

def test_success():
    e = Example()
    result = e.return_1()
    assert result == 1

def test_fail():
    e = Example()
    result = e.return_2()
    assert result == 2
