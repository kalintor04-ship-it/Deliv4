
import pytest
from fraction import Fraction


# 1. Initialization

def test_initialization():
    """Test that a fraction can be created."""
    fraction = Fraction(3, 4)

    assert str(fraction) == "3/4"
    