def emojii_function(message):
    words = message.split(' ')
    emojiis = {
        ":)": "😊",
        ":(": "😒"
    }

    output = ""
    for word in words:
        output += emojiis.get(word, word) + " "
    return output


message = input(">")
print(emojii_function(message))

