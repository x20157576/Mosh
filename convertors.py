def lbs_to_kgs(weight):
    return weight * 0.45

def kg_to_lbs(weight):
    return weight / 0.45

def find_max(list_of_numbers):
    max = list_of_numbers[0]
    for number in list_of_numbers:
        if number > max:
            max = number
    return(max)

