#names = ['Larry', 'Kehrly', 'Moo', 'Bubby', 'Scanny', 'Goggy']
names = [
    "Dunce",
    "Blockhead",
    "Numskull",
    "Dolt",
    "Clod",
    "Dunderhead",
    "Knucklehead",
    "Lunkhead",
    "Chowderhead",
    "Muttonhead",
    "Noodle",
    "Bonehead"
]

# Пример использования
print(names[3])  # Выведет "Dolt"



def num_converter(num):
    dict = {
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
            10: "ten",
            11: "eleven",
            12: "twelve",
            13: "thirteen",
            14: "fourteen",
            15: "fifteen",
            16: "sixteen",
            17: "seventeen",
            18: "eighteen",
            19: "nineteen",
            20: "twenty"
        }
    return dict[num]


def introduce_stooges(names):
    message_2 = ''
    message_1 = f'{num_converter(len(names))[0].upper() + num_converter(len(names))[1:].lower()} balbeses: '
    x = 1
    for name in names:
        message_2 += f'{x}: {name}'
        if x < len(names) - 1:
            message_2 += ', '
        elif x < len(names):
            message_2 += ' and '
        x += 1

    return message_1, message_2



first_string, second_string = introduce_stooges(names)
print(f'{first_string}\n{second_string}')