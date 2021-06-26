from abc import ABC, abstractmethod


class abstract_recipe(ABC):

    def execute(self):
        self.get_ready()
        self.do_the_dishes()
        self.cleanup()

    @abstractmethod
    def get_ready(self):
        pass

    @abstractmethod
    def do_the_dishes(self):
        pass

    @abstractmethod
    def cleanup(self):
        pass


class recipe1(abstract_recipe):

    def get_ready(self):
        print("Getting ready raw materials")


    def do_the_dishes(self):
        print("Do the dish")

    def cleanup(self):
        print('clean utensils and space')

recipe = recipe1()
recipe.execute()
