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

my_bike = Bike(100,10)
my_bike.displayinfo().ride().ride().reverse().ride()
