# decodes a hex character to decimal value
def hex_char_decode(digit):
    if digit == "0":
        return 0
    elif digit == "1":
        return 1
    elif digit == "2":
        return 2
    elif digit == "3":
        return 3
    elif digit == "4":
        return 4
    elif digit == "5":
        return 5
    elif digit == "6":
        return 6
    elif digit == "7":
        return 7
    elif digit == "8":
        return 8
    elif digit == "9":
        return 9
    elif digit == 'a':
        return 10
    elif digit == 'b':
        return 11
    elif digit == 'c':
        return 12
    elif digit == 'd':
        return 13
    elif digit == 'e':
        return 14
    elif digit == 'f':
        return 15

# decodes an entire hex string
def string_to_data(data_string):
    # sets the initally values
    new_val_list = []
    for i in data_string:
        new_val_list.append(hex_char_decode(i))

    return list(new_val_list)

