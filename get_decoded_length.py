def get_decoded_length(rle_data):
    sum_even = 0
    sum_odd = 0

    for i in range(0, len(rle_data), 2):
        sum_even += rle_data[i]
        sum_odd += rle_data[i+1]

    return sum_even