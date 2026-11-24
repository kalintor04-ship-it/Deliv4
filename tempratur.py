
class Temperature:
    """Represent a temperature in Celsius, Fahrenheit or Kelvin."""

    def __init__(self, value: float, unit: str = "C") -> None:
        """Initialize a temperature with a value and unit."""
        unit = unit.upper()

        if unit not in ("C", "F", "K"):
            raise ValueError("Invalid temperature unit")

        if unit == "C" and value < -273.15:
            raise ValueError("Temperature is below absolute zero")

        if unit == "F" and value < -459.67:
            raise ValueError("Temperature is below absolute zero")

        if unit == "K" and value < 0:
            raise ValueError("Temperature is below absolute zero")

        self._value = float(value)
        self._unit = unit

    @property
    def value(self) -> float:
        """Return the temperature value."""
        return self._value

    @property
    def unit(self) -> str:
        """Return the temperature unit."""
        return self._unit

    def to_celsius(self) -> float:
        """Convert temperature to Celsius."""
        if self._unit == "C":
            return self._value

        if self._unit == "F":
            return (self._value - 32) * 5 / 9

        return self._value - 273.15
    

    def to_fahrenheit(self) -> float:
        """Convert temperature to fahrenheit."""
        if self._unit == "F":
            return self._value

        if self._unit == "C":
            return self._value * 9 / 5 + 32

        return (self._value - 273.15) * 9 / 5 + 32

    
    def to_kelvin(self) -> float:
        """Convert temperature to Kelvin."""
        if self._unit == "K":
            return self._value

        if self._unit == "C":
            return self._value + 273.15

        return (self._value - 32) * 5 / 9 + 273.15




    


