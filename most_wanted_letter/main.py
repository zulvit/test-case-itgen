def most_wanted_letter(message):
    message = message.lower()
    count_words = dict()

    for letter in message:
        if letter.isalpha():
            if letter in count_words:
                count_words[letter] += 1
            else:
                count_words[letter] = 1

    max_length = 0
    max_repeat_word = ''
    for k, v in count_words.items():
        if max_length < v:
            max_repeat_word = k
            max_length = v

    if max_repeat_word != '':
        return f'The most popular letter is {max_repeat_word}'
    else:
        return 'There are no letters in the string'


print(most_wanted_letter("......HeLlo......"))
print(most_wanted_letter("String ssss ttAAds TTTTTTT"))
print(most_wanted_letter("!@#$%^&*(*&^%$#@@#$%^&*DFGBQQQQQQQQqqqrrrrrrrr"))
print(most_wanted_letter("!@#$%^&*543234%^&*%$#@345677^%$#@#$%^&"))
print(most_wanted_letter("....пррррривет..."))
print(most_wanted_letter("....Tschüüüüüüüss!..."))

