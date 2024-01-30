# FIXME!!!

def count_runs(flat_data):

    count_of_repeats = 1

    for i in range(1, len(flat_data)):
        if flat_data[i-1] == flat_data[i]:
            count_of_repeats += 1
        else:
            count_of_repeats = 1



    return count_of_repeats


