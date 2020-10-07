# # import utils
# # from utils import find_max
# #
# #
# # list_of_numbers = [243 , 4256, 42, 75335, 245]
# # # print(list_of_numbers)
# # print(find_max(list_of_numbers))
# #
# # print(max(list_of_numbers))
# # from ecommerce import shipping
# #
# # shipping.calc_shipping()
#
# import random
#
#
# #
# # for i in range(5):
# #     print(random.randint(1, 500))
#
# class Dice():
#     def roll(self):
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         return first, second
#
#
# dice = Dice()
# print(dice.roll())

from pathlib import Path

path = Path()
for file in path.glob('*.py'):
    print(file)
