class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_farenheit(self):
        return (self.temperature * 1.8) + 32

man = Celsius(37)

print(man.to_farenheit())
print(man.temperature)