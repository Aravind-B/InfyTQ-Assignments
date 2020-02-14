#PF-TCV-Tryout
import pytest
from Day3.exercise19 import boarding


values=[(0,-1), (2,2),(3,2),(4,1)]

@pytest.mark.parametrize("seat_number,expected_value",values)

def test_boarding(seat_number, expected_value):
    result=boarding(seat_number)
    assert result==expected_value