import pytest
@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("I will execute setps in fictureDemo method")
    def test_fixtureDemo1(self):
        print("I will execute setps in fictureDemo1 method")
    def test_fixtureDemo2(self):
        print("I will execute setps in fictureDemo2 method")
    def test_fixtureDemo3(self):
        print("I will execute setps in fictureDemo3 method")
    def test_fixtureDemo4(self):
        print("I will execute setps in fictureDemo4 method")


#@pytest.fixture()
#def setup():
#    print("I will be executing first")
#    yield
#    print("I will be executed last")
#def test_fixtureDemo(setup):
#    print("I will execute steps in fixtureDemo method")