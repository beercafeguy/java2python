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

class chess_console(gaming_comsole):

    def up(self):
        print("move up")

    def down(self):
        print("move down")

    def left(self):
        print("move left")

    def right(self):
        print("move right")

    def diagonal(self):
        print('move 45 degree')

marop=mario_console()
marop.up()


games=[mario_console(),chess_console()]
for game in games:
    game.up()
    game.down()
    game.left()
    game.right()



class Test1:

    def test(self):
        print('Testing')
    def print(self):
        print("Test1")

class Test2:

    def print(self):
        print("Test2")

tests=[Test1(),Test2()]
for test in tests:
    if isinstance(test,Test1) : test.test()
    test.print()