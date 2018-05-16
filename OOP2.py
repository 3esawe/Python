class Movie:
    def __init__(self, new_name, new_director):
        self.name = new_name
        self.director = new_director
    def print_info(self):
        print (self.name , self.director)

my = Movie('omar', 'ali')
my.print_info()
class Garage:
  def __init__(self):
    self.cars = []

  def __repr__(self):
    return f'Garage {self.cars}'

  def __str__(self):
    return f'Garage with {len(self.cars)} cars'

"""
You should implement at least `__repr__`.

In order to call these methods, you can:
"""

garage = Garage()
garage.cars.append('Fiesta')
garage.cars.append('Focus')

print(garage)
