students = [
    {"name": "Max", "grade": 90},
    {"name": "rolf","grade": 100},

]
for students in students:
    name = students["name"]
    grade = students["grade"]
    print(f"{name} has a grade {grade}.")
    
#range(): to repeat something a certain number of times.

for i in range(20):
    print("i")    
# loop by values 
kids_ages = (3, 5, 7)
for ages in kids_ages:
    print(f"I have a {ages} year old kid. ")    

