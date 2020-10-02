class Student:
    """"Этот класс описывает студента!"""

    def __init__(self,name,last_name):
        self.name = name
        self.surname = last_name

x = Student('Alina','Turganbaeva')
print(x.name,x.surname)
