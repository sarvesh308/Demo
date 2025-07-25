
# By unittest framework
"""
import unittest

# Code to be tested
def add(a,b):
    return a + b

# unit test class
class taf(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3), 5)
        self.assertEqual(add(-1,1), 0)
        self.assertEqual(add(0,0), 0)
        self.assertEqual(add(-1,-1), -2)

if __name__ == '__main__':
    unittest.main()

"""

# By pytest framework

import pytest

def add(a, b):
    return a + b
 
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
 
def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
 
def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)

if __name__ == "__main__":
    pytest.main()