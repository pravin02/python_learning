from functions import double, full_name
import pytest


def test_fun_double():
    assert double(2) == 4


class TestFunctions:

    def setup(self):
        print("setup runs before every single test")

    def teardown(self):
        print("teardown runs after every single test")

    def setup_class(self):
        print("setup_class runs before every single test")

    def teardown_class(self):
        print("teardown_class runs after every single test")

    def test_full_name(self):
        assert full_name("Pravin", "Patil") == "Pravin Patil"


@pytest.mark.parametrize("num", [2, 3, 4, 5])
def test_double(num):
    assert double(num) == num * 2
