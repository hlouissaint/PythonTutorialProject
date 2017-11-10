class Price():
    def __init__(self, vat, discount):
        self.vat = vat
        self.discount = discount


    def final_price(self):
        """Returns price after applying vat and fixed discount."""
        return (self.net_price * (100 + self.vat) / 100) - self.discount



p1 = Price(25,10)
p1.net_price = 100

print (p1.final_price())
print (Price.final_price(p1))
print("The value of vat:", p1.vat)
print("The value of discount:", p1.discount)