import pytest

pytest.mark.xfail
def test_first():
    msg="Hi"
    assert msg=="Hi","Test faild because strings do not match"
@pytest.mark.smoke
def test_credit_card():
    num='enter your number'
    assert 'enter your number'==num