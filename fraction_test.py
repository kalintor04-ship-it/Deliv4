
import pytest
from fraction import Fraction


# 1. Initialization

def test_initialization():
    """Test that a fraction can be created."""
    fraction = Fraction(3, 4)

    assert str(fraction) == "3/4"

# 2. Validation

def test_zero_denominator():
    """Test that zero is not a valid denominator."""
    with pytest.raises(ValueError):
        Fraction(1, 0)


def test_negative_denominator():
    """Test that negative denominators are rejected."""
    with pytest.raises(ValueError):
        Fraction(1, -2)


def test_invalid_numerator():
    """Test that the numerator must be an integer."""
    with pytest.raises(TypeError):
        Fraction(1.5, 2)


def test_invalid_denominator():
    """Test that the denominator must be an integer."""
    with pytest.raises(TypeError):
        Fraction(1, 2.5)
