nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('Found!')
        break # breaking loops
    print(num)

print('------------')

for num in nums:
    if num == 3:
        print('Found!')
        continue # skips the remaining part of this iteration
    print(num)

print('------------')
# Nested Loops

for num in nums:
    for letter in 'abc':
        print(num, letter)

print('------------')

for i in range(1, 11):
    print(i)

print('------------')

x = 0

while x < 10:
    print(x)
    x += 1

print('------------')

x = 0

while True:
    print(x)
    x+=1
