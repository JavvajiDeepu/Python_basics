class student:
    def __init__(self, name, school):
        self.name= name
        self.school= school
        self.marks= []
    def average(self):
        return sum(self.marks) / len(self.marks)
class workingstudent(student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary= salary
#applying decorator to function (@decrorator)
    @property
    def weekly_salary(self):
        return self.salary * 34.6
rolf= workingstudent('Rolf', 'nit', 17.80)
'''print(rolf.salary)
rolf.marks.append(67)
rolf.marks.append(99)
print(rolf.average())
'''
print(rolf.weekly_salary)