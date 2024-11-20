operations= {
    "average": lambda seq: sum(seq)/ len(seq),
    "total": lambda seq: sum(seq),
    "top": lambda seq: max(seq)
}

students= [
    {"name": "rolf","grades":(67,70,90)},
    {"name": "Bob","grades":(100,78,90)},
    {"name":"anne","grades":(100,90,70)}
]
for student in students:
    name= student["name"]
    grades= student["grades"]

    print(f"student:{name}")
    operation=input("enter 'average','total' or 'top':")

    operation_function= operations[operation]
    print(operation_function(grades))