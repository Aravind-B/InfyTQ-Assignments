#PF-TCV-Assgn-29
import pytest
from Day4.assign29 import calculate


def test_calculate_1():
    result=calculate(20,50)
    assert result==3860.0
