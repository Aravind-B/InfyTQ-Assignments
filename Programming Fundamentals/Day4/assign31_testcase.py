#PF-TCV-Assgn-31
import pytest
from Day4.assign31 import check_palindrome

def test_check_palindrome_1():
    result=check_palindrome("GADAG")
    assert result==True