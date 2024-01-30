def hex_char_decode(digit):
    if digit == "0":
        return '0'
    elif digit == 1:
        return '1'
    elif digit == 2:
        return '2'
    elif digit == 3:
        return '3'
    elif digit == 4:
        return '4'
    elif digit == 5:
        return '5'
    elif digit == 6:
        return '6'
    elif digit == 7:
        return '7'
    elif digit == 8:
        return '8'
    elif digit == 9:
        return '9'
    elif digit == 10:
        return 'a'
    elif digit == 11:
        return 'b'
    elif digit == 12:
        return 'c'
    elif digit == 13:
        return 'd'
    elif digit == 14:
        return 'e'
    elif digit == 15:
        return 'f'

def to_hex_string(data):
    total_sum = ""
    index_tracker = 0

    for d in data:
        total_sum += str(hex_char_decode(d))

    return total_sum