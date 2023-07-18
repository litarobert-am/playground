import pytest
from even import is_even

class TestClass:
    def test_one(self):
        assert is_even(20) == True
        assert is_even(12312) == True
        assert is_even(5) == False
        assert is_even(9) == False

    def test_two(self):
        assert is_even(-5) == False
        assert is_even(-4) == True
        assert is_even(0) == True