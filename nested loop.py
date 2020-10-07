# for x in range(9):
#     for y in range(6):
#         print(f'({x},{y})')
    

# numbers = [5, 2, 5, 2, 3]
# for x in numbers:
#     for y in str(x):
#         print('x' * x)


# names = ['John', 'Bob', 'Corin', 'Fred']

# #return last
# print(names[-1])
# 'return from range 2'
# print(names[2:])

# #modify list
# names [0] = 'Jon'
# print(names)

list_of_numbers = [243 , 4256, 42, 75335, 245]

print(list_of_numbers)

list_of_numbers.sort()
for number_length in list_of_numbers:
        print(number_length)
last_number = list_of_numbers[-1]

print(f'The highest number is: {last_number}')

list_of_numbers = [243 , 4256, 42, 75335, 245]

max = list_of_numbers[0]

for number in list_of_numbers:
    if number > max:
     max = number
print(f'The other highest number is: {max}')

