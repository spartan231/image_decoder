# FIXME!!!!

def encode_rle(flat_data):
    count = 1
    num_one = 0
    num_two = 0
    num_val = 0
    encode_list = []

    for i in range(1, len(flat_data)):
        if flat_data[i-1] == flat_data[i]:
            num_val = flat_data[i]
            num_one += 1
            count += 1

        else:
            encode_list.append(count)
            encode_list.append(num_val)
            count = 0

    count += 1
    encode_list.append(count)
    encode_list.append(num_val)

    return encode_list
