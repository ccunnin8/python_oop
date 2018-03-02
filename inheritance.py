class Animal(object):
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print("Health: " + str(self.health))
        return self
# dog = Animal("jo",20)
# dog.walk().walk().walk().run().run()
# dog.display_health()

class Dog(Animal):
    def __init__(self,name):
        Animal.__init__(self,name,health=150)
    def pet(self):
        self.health += 5
        return self

# dog = Dog("jo")
# dog.walk().walk().walk().run().run().pet().display_health()

class Dragon(Animal):
    def __init__(self,name):
        Animal.__init__(self,name,health=170)
    def fly(self):
        self.health += 10
        return self
    def display_health(self):
        Animal.display_health(self)
        print("I am a Dragon")
        return self
# 
# d = Dragon("g")
# d.fly().display_health()
