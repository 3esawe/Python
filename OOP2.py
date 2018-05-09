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
