"""
Calculator Module - Basic arithmetic operations
Students will extend this with more functions
"""

def add(a, b):
    """Add two numbers together"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a * b

def divide(a, b):
    """Divide a by b"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Division requires numeric inputs")
    if b == 0:
        raise ValueError("Cannot divide by zero - division by zero is undefined")
    return a / b
class TestAdvancedOperations:
     """Test power and square root operations"""

def test_power_positive_numbers(self):
    """Test power with positive numbers"""
    assert power(2, 3) == 8
    assert power(5, 2) == 25

def test_power_zero_exponent(self):
    """Test power with zero exponent"""
    assert power(5, 0) == 1
    assert power(0, 0) == 1

def test_square_root_positive_numbers(self):
    """Test square root of positive numbers"""
    assert square_root(4) == 2
    assert square_root(9) == 3
    assert square_root(16) == 4

def test_square_root_negative_raises_error(self):
    """Test that square root of negative raises
    ValueError""" 
    with pytest.raises(ValueError, match="Cannot
calculate square root of negative"):
 square_root(-4)

# TODO: Students will add power, sqrt functions

if __name__ == "__main__":
    print("🧮 Calculator Module")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")