class Bike(object):
    def __init__(self,price,max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayinfo(self):
        '''
        Prints price, max_speed, miles to console
        Returns self
        '''
        print("""Price: {price},
                 Max Speed: {max_speed}
                 Total Miles: {miles}""".format(price=self.price,
                 max_speed=self.max_speed,miles=self.miles))
        return self

    def ride(self):
        """
        Prints 'riding' to console and increases miles by 10
        Returns self
        """
        print("Riding")
        self.miles += 10
        return self

    def reverse(self):
        """
        Prints 'Reversing' to console, decreases miles by 5
        Returns self
        """
        print("Reversing")
        self.miles -= 5
        return self

# my_bike = Bike(100,10)
# my_bike.displayinfo().ride().ride().reverse().ride()

class Car(object):
    def __init__(self,price,speed,fuel,mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12

    def display_all(self):
        """
        Prints attributes to console, return self
        """
        print("Price: " + str(self.price))
        print("Speed: " + str(self.speed) + "mph")
        print("Fuel: " + self.fuel)
        print("Mileage: " + str(self.mileage) + "mpg")
        print("Tax: " + str(self.tax))
        return self

car1 = Car(20000,35,"Full",105)
car1.display_all()
