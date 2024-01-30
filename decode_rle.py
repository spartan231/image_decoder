import itertools
def decode_rle(rle_data):
    num_list = []
    new_list = []


    for i in range(0, len(rle_data), 2):
        # FIXME
        num_list.append(rle_data[i] * str(rle_data[i+1]).split())

        #new_list.append(rle_data[i] * str(rle_data[i+1]))

    return list(itertools.chain.from_iterable(num_list))