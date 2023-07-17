courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)
print(len(courses))
print(courses[2])
print(courses[-1]) # Returns the last item in the list

# "Slicing'
print(courses[0:2]) # First index is inclusive, second is not
print(courses[:2]) # First index is inclusive, second is not
print(courses[2:])

# Append
courses.append('Art')
print(courses)

# Insert
courses.insert(0, 'Art')
print(courses)

# Extend vs Append
courses_2 = ['Art', 'Education']
# courses.insert(0, courses_2)
print(courses) # Adds a list within a list
print(courses[0][0]) # Adds a list within a list

courses.extend(courses_2)
print(courses)

# Remove
courses.remove('Math')
print(courses)

# Pop - Removes last item and returns it
popped = courses.pop()
print(popped)

# Reverse
courses.reverse()
print(courses)

# Sort
courses.sort()
print(courses)

courses.sort(reverse=True)
print(courses)

# Get a sorted version of a list without editing the original
sorted_courses = sorted(courses)
print(sorted_courses)

# min,max
nums = [1,5,2,4,3]
print(sorted(nums))
print(min(nums))
print(max(nums))
print(sum(nums))