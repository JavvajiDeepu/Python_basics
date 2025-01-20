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
    
#magic methods
class club:
    def __init__(self, name):
        self.name= name
        self.player= []

    def __len__(self):
        return len(self.player)
    
    def __getitem__(self,i):
        return self.player[i]
    
    def __repr__(self):
        return f"club{self.name}:{self.player}"
    
    def __str__(self):
        return f"club{self.name}with {len(self)} player"
    


 
