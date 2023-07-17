# Dictionaries are Hash Maps
student = {'name':'John', 'age':25, 'courses':['Math', 'Compsci']}

student['phone'] = '555-5555'
student['name'] = 'Jane'

print(student['name'])
print(student.get('phone', 'Not Found'))

print('-----------')

student.update({'name':'Jane', 'age':26})

#del student['age']
age = student.pop('age')
print(age)
print(student)

print(len(student))
print(student.keys())
print(student.values())
print(student.items())

print('-----------')

for key in student:
    print(key)

print('-----------')

for key, value in student.items():
    print(key, value)