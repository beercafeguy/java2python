class Book:

    def __init__(self, name,no_of_copies):
        self.name = name
        self.no_of_copies=no_of_copies

    def __repr__(self):
        return repr((self.name,str(self.no_of_copies)))

    def inc_no_of_books(self, how_much=1):
        self.no_of_copies += how_much

    def dec_no_of_copies(self, how_much=1):
        self.no_of_copies -= how_much

book1 = Book('Mastering Python', no_of_copies=10)
book2 = Book(name='Mastering GCP', no_of_copies=2)

print(book1)
print(book2)
book1.inc_no_of_books()
book2.inc_no_of_books(10)
book2.dec_no_of_copies()
print(book1)
print(book2)
