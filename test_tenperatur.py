
from temperature import Temperature

temp1 = Temperature(25, "C")
temp2 = temp1.convert_to("F")
temp3 = temp1.convert_to("K")

print(temp1)
print(temp2)
print(temp3)

print(repr(temp1))
