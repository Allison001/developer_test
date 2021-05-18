import pytest

def test_success():
    """this test succeeds"""
    assert True

@pytest.mark.xfail(condition=lambda:True,reason="this test is expecting failure")
def test_failure():
    """this test fails"""
    assert False


def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')


def test_broken():
    raise Exception('oops')