#PF-TCV-Tryout
import pytest
from Day3.exercise19 import boarding

def test_boarding_1():
    result=boarding(3)
    assert result==1

def test_boarding_2():
    result=boarding(24)
    assert result==1