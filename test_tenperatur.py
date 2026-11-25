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

# 4. Round-trip conversions

def test_round_trip():
    """Test that round-trip conversions preserve temperature."""
    original = Temperature(25, "C")

    fahrenheit = original.convert_to("F")
    kelvin = fahrenheit.convert_to("K")
    celsius = kelvin.convert_to("C")

    assert celsius == original
    assert celsius.unit == "C"
    assert celsius.value == pytest.approx(25)

    # 5. Cross-unit comparisons

def test_comparisons():
    """Test comparisons across different units."""
    temp1 = Temperature(0, "C")
    temp2 = Temperature(32, "F")
    temp3 = Temperature(100, "C")

    assert temp1 == temp2
    assert temp1 != temp3
    assert temp1 < temp3
    assert temp1 <= temp2
    assert temp3 > temp1
    assert temp3 >= temp1

# 6. Formatting

def test_str():
    """Test the human-readable representation."""
    temp = Temperature(25, "C")

    assert str(temp) == "25.00 °C"


def test_repr():
    """Test the unambiguous representation."""
    temp = Temperature(25, "C")

    assert repr(temp) == "Temperature(25.0, 'C')"


# 7. Additional tests

def test_tolerance():
    """Test floating-point comparison tolerance."""
    temp1 = Temperature(25, "C")
    temp2 = Temperature(25 + 1e-10, "C")

    assert temp1 == temp2


def test_invalid_target_unit():
    """Test that invalid conversion units are rejected."""
    temp = Temperature(25, "C")

    with pytest.raises(ValueError):
        temp.convert_to("X")


def test_absolute_zero_conversion():
    """Test conversion at the lowest possible temperature."""
    temp = Temperature(-459.67, "F")
    converted = temp.convert_to("K")

    assert converted.value == pytest.approx(0, abs=1e-9)

