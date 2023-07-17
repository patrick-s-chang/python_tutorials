from Student import Student

student1 = Student("Patrick", "Mechanical Engineering", 4.0, False)
student2 = Student("Farquad", "Political Science", 2.0, True)

print(student2.gpa)
print(student1.name)
print(student2.name)
print(student1.on_honor_roll())
print(student2.on_honor_roll())