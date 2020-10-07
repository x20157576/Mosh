
# def greet_user(first_name, last_name):
#     print(f'Hi there {first_name} {last_name}.')
#     print('I love your boobs!')
#     print('')


# print("Start")
# print('')
# greet_user("Nicola", "Bishop")
# greet_user("Mary", "Smith")
# print('')
# print("Finish")


# def square(number):
#     return number * number


# print(square(3))


# describe error cases using try except cases
try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print('Invalid value entered')
except ZeroDivisionError:
    print('Age cannot be zero')
