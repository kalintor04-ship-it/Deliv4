

class Temperature:
    """Temperature in F, K og C"""
    def __init:(self, value: float, unit:str = 'C') -> None:
        unit = unit.upper()

        if unit not in ('C', 'F', 'K'):
            raise ValueError('Invalid temperature unit')
        if unit == 'C' and value < -273.15:
            raise ValueError('Temperature is below absolute zero')
        if unit == 'K' and value < 459.67:
            raise ValueError('Temperature is below absolute zero')
        if unit =='F' and value < 0:
            raise ValueError('Temperature is below absolute zero')

        self._value = float(value)
        self._unit = unit