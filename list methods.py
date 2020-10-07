numbers = [50 , 50, 42, 75335, 245]
numbers2 = numbers.copy()

print(numbers)

numbers.append(20)

print(numbers)

numbers.insert(0, 10)

print(numbers)

numbers.remove(42)

print(numbers)

numbers.pop()

print(numbers)

print(numbers.index(245))

#bool result
print(50 in numbers)

#count in list
print(numbers.count(50))

print(numbers.sort())

print(numbers)

print(numbers.reverse())

print(numbers)

print(f'Original List is {numbers2} and the new list is {numbers}')

