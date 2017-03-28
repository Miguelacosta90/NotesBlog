class car(object):
    def __init__(self, speed, fuel, mileage):
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.price = 2000
        self.tax = .12

    def displayInfo(self):
        print self.speed, self.fuel, self.mileage, self.price, self.tax
        return self

car = car("20mph","half full", 20).displayInfo()
