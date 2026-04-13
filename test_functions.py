from functions import double, full_name
import pytest

def test_fun_double():
    assert double(2) == 4


class TestFunctions:   
    
    def test_full_name(self):
        assert full_name("Pravin", "Patil") == "Pravin Patil"


@pytest.mark.parametrize("num", [2,3,4,5])
def test_double(num):
    assert double(num) == num * 2