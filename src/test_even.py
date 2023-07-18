import pytest
from even import is_even

class TestClass:
    def test_one(self):
        assert isEven(20) == True
        assert isEven(12312) == True
        assert isEven(5) == False
        assert isEven(9) == False

    def test_two(self):
        assert isEven(-5) == False
        assert isEven(-4) == True
        assert isEven(0) == True