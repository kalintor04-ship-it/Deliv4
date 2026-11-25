
import pytest
from tempratur import Temperature


#Innitialization
def test_default_unit():
    """Test that Celsius is the default unit."""
    temp = Temperature(20)

    assert temp.unit == "C"
    assert temp.value == 20


def test_case_insensitive_unit():
    """Test that lowercase units are accepted."""
    temp = Temperature(20, "c")

    assert temp.unit == "C"


def test_read_only_value():
    """Test that the value cannot be changed."""
    temp = Temperature(20, "C")

    with pytest.raises(AttributeError):
        temp.value = 30


def test_read_only_unit():
    """Test that the unit cannot be changed."""
    temp = Temperature(20, "C")

    with pytest.raises(AttributeError):
        temp.unit = "F"

#Valitation
def test_invalid_unit():
    """Test that invalid units are rejected."""
    with pytest.raises(ValueError):
        Temperature(20, "X")

def test_below_absolute_zero_celsius():
    """Test that temperatures below absolute zero are rejected."""
    with pytest.raises(ValueError):
        Temperature(-274, "C")

def test_below_absolute_zero_fahrenheit():
    """Test invalid Fahrenheit temperatures."""
    with pytest.raises(ValueError):
        Temperature(-460, "F")


def test_below_absolute_zero_kelvin():
    """Test invalid Kelvin temperatures."""
    with pytest.raises(ValueError):
        Temperature(-1, "K")
# 3. Conversions

def test_absolute_zero():
    """Test conversions at absolute zero."""
    temp = Temperature(-273.15, "C")

    assert temp.to_fahrenheit() == pytest.approx(-459.67)
    assert temp.to_kelvin() == pytest.approx(0)


def test_crossover():
    """Test conversions at minus 40 degrees."""
    temp = Temperature(-40, "F")

    assert temp.to_celsius() == pytest.approx(-40)
    assert temp.to_kelvin() == pytest.approx(233.15)


def test_freezing_point():
    """Test conversions at the freezing point of water."""
    temp = Temperature(273.15, "K")

    assert temp.to_celsius() == pytest.approx(0)
    assert temp.to_fahrenheit() == pytest.approx(32)


def test_body_temperature():
    """Test conversions at human body temperature."""
    temp = Temperature(37, "C")

    assert temp.to_fahrenheit() == pytest.approx(98.6)
    assert temp.to_kelvin() == pytest.approx(310.15)


def test_boiling_point():
    """Test conversions at the boiling point of water."""
    temp = Temperature(212, "F")

    assert temp.to_celsius() == pytest.approx(100)
    assert temp.to_kelvin() == pytest.approx(373.15)