# Generated from: temperature_and_fractions.ipynb
# Converted at: 2026-11-26T15:21:12.905Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # Python Assignment: Temperatures and Fractions
# 
# This notebook demonstrates the two classes I implemented: Temperature (in temperature.py) and Fraction (in fraction.py). Each section shows the class in use, and the last section runs the pytest test files (test_temperature.py and test_fraction.py).


# #Task 1 – Temperature
# 
# My Temperature class stores the value in its original unit (C, F or K) and has the following features:
# 
# The unit is case-insensitive and defaults to "C"; the value must be a number (not a bool).
# #value and unit are read-only properties.
# Temperatures below absolute zero raise a ValueError.
# Conversion with to_celsius(), to_fahrenheit(), to_kelvin() and convert_to(unit), which returns a new Temperature.
# ==, !=, <, <=, >, >= compare across units (via Kelvin) using a tolerance of 1e-9.
# __str__ and __repr__ for readable and developer-friendly output.


# Creating temperatures and printing them


from temperature import Temperature

t = Temperature(25)            # unit defaults to Celsius
print(t)                       # __str__
print(repr(t))                 # __repr__
print(Temperature(32, 'f'))    # lowercase unit is accepted
print(Temperature(300, 'K'))

# Conversions


boiling = Temperature(100, 'C')
print('100 C in F:', boiling.to_fahrenheit())
print('100 C in K:', boiling.to_kelvin())
print('98.6 F in C:', Temperature(98.6, 'F').to_celsius())

# convert_to returns a new Temperature object
print(Temperature(0, 'C').convert_to('F'))
print(repr(Temperature(37, 'C').convert_to('K')))

# Comparisons across units


print(Temperature(0, 'C') == Temperature(32, 'F'))
print(Temperature(0, 'C') != Temperature(10, 'C'))
print(Temperature(-10, 'C') < Temperature(32, 'F'))
print(Temperature(100, 'C') > Temperature(32, 'F'))
print(Temperature(0, 'C') <= Temperature(32, 'F'))
print(Temperature(0, 'C') >= Temperature(32, 'F'))

# #Validation and read-only attributes


def try_it(label, func):
    try:
        func()
    except Exception as e:
        print(f'{label}: {type(e).__name__}: {e}')

try_it('Below absolute zero', lambda: Temperature(-300, 'C'))
try_it('Invalid unit', lambda: Temperature(10, 'X'))
try_it('Invalid value', lambda: Temperature('hot', 'C'))
try_it('Invalid target unit', lambda: Temperature(10, 'C').convert_to('Rankine'))

t = Temperature(25)
try_it('Changing value', lambda: setattr(t, 'value', 30))
try_it('Changing unit', lambda: setattr(t, 'unit', 'F'))

# # Task 2 – Fraction
# 
# My Fraction class stores a normalized fraction (lowest terms, strictly positive denominator) and has the following features:
# 
# Both numerator and denominator must be integers (not float or bool), otherwise TypeError; denominator 0 raises ValueError.
# Fractions are normalized automatically using gcd, and a negative denominator moves the sign to the numerator.
# numerator and denominator are read-only properties.
# All six comparison operators, with int accepted on the other side.
# +, -, *, / (also with int), unary -, abs() and float().
# Dividing by a zero fraction raises ZeroDivisionError.


# Creating and normalizing fractions


from fraction import Fraction

print(Fraction(2, 4))        # reduced to 1/2
print(Fraction(1, -2))       # sign moved to numerator
print(Fraction(-2, -4))      # two negatives cancel
print(Fraction(5))           # denominator defaults to 1
print(repr(Fraction(3, 4)))

# Arithmetic


a = Fraction(1, 2)
b = Fraction(1, 3)

print('a + b =', a + b)
print('a - b =', a - b)
print('a * b =', a * b)
print('a / b =', a / b)
print('a + 1 =', a + 1)       # int on the right is allowed

# Comparisons


print('a == Fraction(2, 4):', a == Fraction(2, 4))
print('a != b:', a != b)
print('a < b:', a < b)
print('a <= b:', a <= b)
print('a > b:', a > b)
print('a >= b:', a >= b)

# Negation, absolute value and float conversion


print(-a)
print(abs(Fraction(-2, 3)))
print(float(a))
print(float(Fraction(1, 4)))

# #Validation


try_it('Zero denominator', lambda: Fraction(1, 0))
try_it('Float numerator', lambda: Fraction(1.5, 2))
try_it('Float denominator', lambda: Fraction(1, 2.5))
try_it('Division by zero', lambda: Fraction(1, 2) / Fraction(0, 5))

# Pytest results
# 
# Both test files are run with pytest. There are 15 tests for Temperature (counting each parametrized case) and 6 tests for Fraction, 21 in total. 


import sys
!{sys.executable} -m pytest -q test_temperature.py test_fraction.py

# 
# task 1
# We start with the Temperature class. You create a temperature with a number and a unit: C for Celsius, F for Fahrenheit, or K for Kelvin. If you don't write a unit, it uses Celsius.
# The class can convert between the units. For example, 100 degrees Celsius is 212 degrees Fahrenheit and 373.15 Kelvin. The method convert_to gives you a new temperature object in the unit you choose.
# You can also compare temperatures, even with different units. For example, 0 degrees Celsius is equal to 32 degrees Fahrenheit. The code converts both to Kelvin first, and it uses a small tolerance, so tiny decimal errors don't cause problems.
# The class also checks the input. A temperature can't be below absolute zero, and the unit must be C, F or K. The value and unit are read-only, so you can't change them after you create the object.
# 
# 
# task 2
# A fraction has a numerator and a denominator, and both must be integers. The denominator can't be zero.
# The class makes every fraction as simple as possible. For example, 2 over 4 becomes 1 over 2. If the denominator is negative, the minus sign moves to the numerator.
# You can add, subtract, multiply and divide fractions. For example, 1/2 plus 1/3 is 5/6. You can also use whole numbers, like 1/2 plus 1.
# We can compare fractions with all six operators, like less than and greater than or equal. We can also use minus, absolute value, and convert a fraction to a float. If you divide by a fraction that is zero, the code gives a ZeroDivisionError.
# Finally, the tests. We used pytest to check both classes. There are 21 tests in total: 15 for Temperature and 6 for Fraction. They test normal cases and also error cases.
# 
# Link til GitHub: https://github.com/kalintor04-ship-it/Deliv4.git
#