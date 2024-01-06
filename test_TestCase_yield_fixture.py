import pytest


@pytest.yield_fixture() # Starting from pytest version 3.0.0, @pytest.yield_fixture has been deprecated
def setup():
    print("Once before every method")
    yield
    print("Once after every method")


def testMethod1(setup):
    print("This is Test Method1")


def testMethod2(setup):
    print("This is Test Method2")