# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


message = """
Hello World
my name is Patrick
"""
print(message.replace('World','Penis'))

greeting = 'Hello'
name = 'Patrick'
message2 = greeting + ', ' + name + '. Welcome!'
print(message2)

message3 = '{}, {}. Welcome!'.format(greeting, name)
print(message3)

message4 = f'{greeting}, {name}. Welcome!'
print(message4)

print(dir(message4))

print(help(str))