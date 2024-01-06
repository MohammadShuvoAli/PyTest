import pytest


@pytest.fixture() # executes specific method before & after every test method
def setup():
    print("Once before every method")
    yield
    print("Once after every method")


def testMethod1(setup):
    print("This is Test Method1")


def testMethod2(setup):
    print("This is Test Method2")