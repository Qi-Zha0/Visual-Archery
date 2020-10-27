import math
import pytest

def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

def test_square():
   num = 7
   assert 7*7 == 49

@pytest.mark.others
def test_quality():
   assert 10 == 10