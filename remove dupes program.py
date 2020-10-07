numbers = [50 , 50, 42, 75335, 245, 245, 50]

uniques = []
#
for number in numbers:
    if number not in uniques:
        uniques.append(number)
#
#
print(uniques)
