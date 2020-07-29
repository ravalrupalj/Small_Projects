#Any pytest file should start with test_ or end with _test
#pytest method names should start with test
#Any code should be wrapped in method only
#Method name should make sense
# -k stands for method name execiton, -s logs in out put -v stands for more info metadata
# Single file=you can run specific file with py.test <filename>
# Single method=py.test (file name)::method name
# run method with specific word=py.test -v -k "Program"
# you can mark(tag)tests @pytest.mark.smoke and then run with -m
# you can skip tests with @pytest.mark.skip
#pytest.mark.xfail
#Fixtures are used as setup and tear down methods for test cases-conftest file to gerneralize
#fixture and make it available to all test cases
#datadriven and parameterization can be done with return statments in list format
# when you define fixture scope ot class only, it will run once before class is initiated and at the end
import pytest

@pytest.mark.skip
def test_firstProgram():
    print("Hello")
@pytest.mark.smoke
def test_secondProgram(setup):
   print("Good Morning")
def test_credit_card():
    name='rupal'
    assert name=='rupal' , "name does not match"
def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
