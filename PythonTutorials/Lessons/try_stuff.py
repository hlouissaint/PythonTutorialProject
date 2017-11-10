import tempfile
import os

class Vehicle(object):
    name = ""
    kind = ""
    color = ""
    value = 100.00

    def description(self):
        desc_str = "%s is a %s %s %s worth %.2f." % (self.name, self.color, self.name, self.kind, self.value)
        return desc_str


car1 = Vehicle()
car1.name = "Toyota"
car1.color = "black"
car1.kind = "sedan"
car1.value = 25000.00
print(car1.description())

