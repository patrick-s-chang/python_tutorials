# Object Identity: is

language = 'Java'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
elif language == 'Javascript':
    print('Language is Javascript')
else:
    print('No match')

## Python doesn't have switches, so if, elif, and else are sufficient


# and
# or
# not

user = 'Admin'
logged_in = False
if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

print('---------------')

if not logged_in:
    print('Please log in')
else:
    print('Welcome')

print('---------------')
# Object Identity -> checks if the two things being compared are the same objects in memory

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)

c = a
print(a is c)
print(a == b)

print(id(a))
print(id(b))
print(id(c))
print(id(a) == id(b))
print(id(a) == id(c))

print('---------------')
# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.
condition = ()

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')