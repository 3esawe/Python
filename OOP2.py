<<<<<<< HEAD
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
=======
class averge:
    """docstring for ."""
    def __init__(self, name,grades):
        self.name = name
        self.grades = grades
    def averge(self):
        print('the averge for' , self.name ,' is ' , sum(self.grades) / len(self.grades))
omar = averge('omar' , [25,90,13,70])
omar.averge()


class Garage:
    """docstring for ."""
    def __init__(self):
        self.cars = []
    def __len__ (self):
        return (len(self.cars))
    def __getitem__ (self ,i):
        return self.cars[i]
    def __repr__(self):
        return 'Garage {}'.format(self.cars)
    def __str__(self):
        return 'Garage with {} cars'.format(len(self.cars))

Ford = Garage()
Ford.cars.append('GT300')
print(str(Ford))
>>>>>>> e8d844a95b03c9eb6712a13a3f90ae58b851f57b
