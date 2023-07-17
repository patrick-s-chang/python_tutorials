courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses)

print(courses.index('CompSci'))

print('Art' in courses)
print('CompSci' in courses)

# for loop
for item in courses:
    print(item)

# for loop + enumeration
for index, course in enumerate(courses, start=1):
    print(index, course)

# joining into a string
course_str = ' - '.join(courses)

print(course_str)

# splitting back into a list
new_list = course_str.split(' - ')
print(new_list)

# Strings vs. Tuples
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)

# Tuples (are immutable, the code below doesn't work)
# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# tuple_2 = tuple_1
#
# print(tuple_1)
# print(tuple_2)
#
# tuple_1[0] = 'Art'
#
# print(tuple_1)
# print(tuple_2)

# Sets don't care about order. Also throw away duplicates
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
art_courses = {'History', 'Math', 'Physics', 'Design'}

print(cs_courses.intersection(art_courses)) #courses shared by both cs and art
print(cs_courses.difference(art_courses)) #courses in sc that are not in art
print(cs_courses.union(art_courses)) # adds unique entries from art to cs

# Empty lists, tuples, and sets
empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = {} # This is wrong! It's a dictionary
empty_set = set()