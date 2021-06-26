class Person:

    def __init__(self,name,address):
        self.name=name
        self.address=address

    def __repr__(self):
        return repr((self.name,self.address))


class Student(Person):

    def __init__(self, name,address, college,year):
        super().__init__(name,address)
        self.college = college
        self.year=year


    def __repr__(self):
        return repr((super().__repr__(),self.college,self.year))


person=Person('Hem','Haldwani')
student=Student('Nidhi', 'Delhi','DU','2013')

print(person)
print(student)


class Earth:
    pass

earth=Earth()
