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
#
# car1 = Car(20000,35,"Full",105)
# car1.display_all()

class Product(object):
    def __init__(self,price,item_name,weight,brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

    def sell(self):
        """
        change self.status -> 'sold'
        return self
        """
        self.status = "sold"
        return self

    def add_tax(self,tax):
        """
        returns the price w tax
        """
        return self.price + (self.price * tax)

    def return_item(self,reason):
        """
        if reason=defective, change status to defective, price to 0
        if reason=unopened, change status to for sale
        if reason=opened, change status to used, price = price - 20%
        return self
        """
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "unopened":
            self.status = "for sale"
        else:
            self.status = "used"
            self.price -= (.20 * self.price)
        return self


cups = Product(10,"cups",1,"GE")
plates = Product(15,"plates",2,"NA")
knives = Product(2,"knives",1,"BBB")

class Store(object):
    def __init__(self):
        self.products = []
        self.location = ""
        self.owner = ""
    def set_owner(self,owner):
        self.owner = owner
        return self
    def set_location(self,location):
        self.location = location
    def add_product(self,product):
        self.products.append(product)
        return self
    def remove_product(self,product):
        index = self.products.index(product)
        del(self.products[index])
        return self

    def inventory(self):
        for product in self.products:
            print("Name: {x}, Price: {y}, Status: {z}".format(
                x=product.item_name, y=product.price, z=product.status
            ))

# our_store = Store()
# our_store.add_product(cups).add_product(knives).add_product(plates)
# our_store.set_owner("corey c")
# our_store.set_owner("washington dc")
# our_store.inventory()
