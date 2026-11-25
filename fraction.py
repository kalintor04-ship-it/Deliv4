
class Fraction:
    """Represent a fraction with a numerator and denominator."""

    def __init__(self, numerator: int, denominator: int) -> None:
        """Initialize and validate a fraction."""
        if type(numerator) is not int:
            raise TypeError("Numerator must be an integer")

        if type(denominator) is not int:
            raise TypeError("Denominator must be an integer")

        if denominator <= 0:
            raise ValueError("Denominator must be positive")

        self._numerator = numerator
        self._denominator = denominator

    def __str__(self) -> str:
        """Return a human-readable representation."""
        return f"{self._numerator}/{self._denominator}"

    def __repr__(self) -> str:
        """Return an unambiguous representation."""
        return f"Fraction({self._numerator}, {self._denominator})"

    def __eq__(self, other: object) -> bool:
        """Check whether two fractions are equal."""
        if not isinstance(other, Fraction):
            return NotImplemented

        return (
            self._numerator * other._denominator
            == other._numerator * self._denominator
        )

    def __lt__(self, other: object) -> bool:
        """Check whether one fraction is smaller."""
        if not isinstance(other, Fraction):
            return NotImplemented

        return (
            self._numerator * other._denominator
            < other._numerator * self._denominator
        )

    def __ne__(self, other: object) -> bool:
        """Check whether two fractions are different."""
        if not isinstance(other, Fraction):
            return NotImplemented

        return not (self == other)

    def __le__(self, other: object) -> bool:
        """Check whether a fraction is smaller or equal."""
        if not isinstance(other, Fraction):
            return NotImplemented

        return self < other or self == other

    def __gt__(self, other: object) -> bool:
        """Check whether a fraction is greater."""
        if not isinstance(other, Fraction):
            return NotImplemented

        return other < self

    def __ge__(self, other: object) -> bool:
        """Check whether a fraction is greater or equal."""
        if not isinstance(other, Fraction):
            return NotImplemented

        return other < self or self == other

    def __add__(self, other: object) -> "Fraction":
        """Add two fractions."""
        if not isinstance(other, Fraction):
            return NotImplemented

        numerator = (
            self._numerator * other._denominator
            + other._numerator * self._denominator
        )
        denominator = self._denominator * other._denominator

        return Fraction(numerator, denominator)

    def __float__(self) -> float:
        """Convert a fraction to a floating-point number."""
        return self._numerator / self._denominator
