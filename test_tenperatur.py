from temperature import Temperature

temp1 = Temperature(25, "C")
temp2 = Temperature(32, "f")
temp3 = Temperature(300, "K")

print(temp1._value, temp1._unit)
print(temp2._value, temp2._unit)
print(temp3._value, temp3._unit)
