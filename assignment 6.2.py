class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print("Name: ", self.name)
        print("Age: ", self.age)

    def get_info(self):
        print("Coat Color: ", self.coat_color)


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, size):
        super().__init__(name, age, coat_color)
        self.size = size

    def bark(self):
        print("Jack Russell Terrier is barking!")

    def play(self):
        print("Jack Russell Terrier is playing!")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color, weight):
        super().__init__(name, age, coat_color)
        self.weight = weight

    def snore(self):
        print("Bulldog is snoring!")

    def eat(self):
        print("Bulldog is eating!")


# Create objects of Dog, JackRussellTerrier, and Bulldog classes
dog1 = Dog("Buddy", 5, "Brown")
dog2 = JackRussellTerrier("Max", 3, "White and Brown", "Small")
dog3 = Bulldog("Rocky", 7, "Fawn", "Medium")

# Call methods on Dog object
dog1.description()
dog1.get_info()

# Call methods on JackRussellTerrier object
dog2.description()
dog2.get_info()
dog2.bark()
dog2.play()

# Call methods on Bulldog object
dog3.description()
dog3.get_info()
dog3.snore()
dog3.eat()
