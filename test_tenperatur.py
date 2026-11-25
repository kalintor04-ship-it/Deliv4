
from tempratur import Temperature

temp1 = Temperature(0, "C")
temp2 = Temperature(32, "F")
temp3 = Temperature(100, "C")

print("Temperature 1:", temp1.to_kelvin())
print("Temperature 2:", temp2.to_kelvin())
print("Temperature 3:", temp3.to_kelvin())

print("Comparison 1:", temp1 == temp2)
print("Comparison 2:", temp1 == temp3)
