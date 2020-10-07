phone_number = input("Phone: ")
number_to_text = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}

output = ""
for ch in phone_number:
    output += number_to_text.get(ch, "!") + " "
print(output)

