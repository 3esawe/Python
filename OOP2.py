class averge:
    """docstring for ."""
    def __init__(self, name,grades):
        self.name = name
        self.grades = grades
    def averge(self):
        print('the averge for' , self.name ,' is ' , sum(self.grades) / len(self.grades))
omar = averge('omar' , [25,90,13,70])
omar.averge()
