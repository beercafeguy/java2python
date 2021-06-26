from abc import ABC,abstractmethod

class gaming_comsole(ABC):

    @abstractmethod
    def up(self):
        pass

    @abstractmethod
    def down(self):
        pass

    @abstractmethod
    def left(self):
        pass

    @abstractmethod
    def right(self):
        pass

class mario_console(gaming_comsole):

    def up(self):
        print("mario up")

    def down(self):
        print("mario down")

    def left(self):
        print("mario left")

    def right(self):
        print("mario right")

    def jump(self):
        print('mario jump')


marop=mario_console()
marop.up()