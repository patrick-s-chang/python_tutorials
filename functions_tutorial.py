def hello_func():
    return 'Hello Function.'

# print(hello_func)  # prints function location in memory

print(hello_func().upper())

# Keeping your code DRY (Don't Repeat Yourself)

def hello_funct(greeting, name = 'Bitch'):
    return '{}, {}, Function.'.format(greeting, name)

print(hello_funct('Hi'))
print(hello_funct('Hi','Patrick'))


print('---------------')
def student_info(*args, **kwargs): #args and kwargs are standard values
    print(args)
    print(kwargs)

student_info('Math', 'Art', name="John", age=22) #Returns a tuple with all the arguments

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

# student_info(courses, info) # Doesn't unpack values
student_info(*courses, **info) # Does unpack values


print('---------------')

# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, False for non-leap years.""" # Three quotes are "doc strings" used to describe what functions are supposed to do.

    return year % 4 == 0 and (year%100 != 0 or year%400 == 0)

def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(is_leap(2018))
print(is_leap(2020))

print(days_in_month(2017, 2))
print(days_in_month(2020, 2))
print(days_in_month(2017, 12))
print(days_in_month(2017, 9))
print(days_in_month(2017, 13))