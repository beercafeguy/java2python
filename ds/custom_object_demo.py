from operator import attrgetter

class Country:

    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area

    def __repr__(self):
        return repr((self.name, self.population, self.area))


countries = [Country('India', '1000', '100'),
             Country('Pakistan', '40', '20'),
             Country('Bangladesh', '50', '30')]

for country in sorted(countries, key=lambda c: int(c.population)):
    print(country)

countries.sort(key=lambda c: len(c.name))
print(countries)
