# Student(college,year) is a Person (name,address)
class LandAnimal:

    def who(self):
        print('I M LandAnimal')

    def walk(self):
        print("walking")

class WaterAnimal:

    def who(self):
        print('I am Water Animal')

    def swim(self):
        print("swimming")

class Amphibian(WaterAnimal,LandAnimal):
    pass


amp = Amphibian()
amp.walk()
amp.who()