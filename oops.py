my_student = {
    'name': 'ROLF',
    'grades': [60, 77,90],
    'average': [86,90,77]
    }
def average_grade(student):
    return sum (student['grades']) / len(student['grades'])

class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades
    def average(self):
        return (self.grades) / len(self.names)

student_one = Student('Rolf Smith' ,[70,80,56,77])
student_two = Student('Jose',[50,45,89,100])
print(student_two.name)
print(student_one.name)
    

## Define a movie  class that has two properties:
class Movie:
        def _init_(self, new_name, new_director):
            self.name = new_name
            self.director = new_director

my_movie = Movie('the Matrix','Wachowski')

