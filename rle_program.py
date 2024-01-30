# imports the console_gfx file
from console_gfx import ConsoleGfx

import itertools


# prints out the spectrum image
print("Welcome to the RLE image encoder!")
print()
print("Displaying Spectrum Image: ")
ConsoleGfx.display_image(ConsoleGfx.test_rainbow)

# prints the menu for the user
def rle_menu():
    print()
    print("RLE Menu")
    print("-" * 8)
    print("0. Exit")
    print("1. Load File")
    print("2. Load Test Image")
    print("3. Read RLE String")
    print("4. Read RLE Hex String")
    print("5. Read Data Hex String")
    print("6. Display Image")
    print("7. Display RLE String")
    print("8. Display Hex RLE Data")
    print("9. Display Hex Flat Data")
    print()

# counts the number of runs within the data set
# takes in a rle list
def count_runs(flat_data):
    # counts the nujmber of 
    count_of_repeats = 0
    updated_list = []

    # iterates from 0 to the length of the flat_data
    for i in range(0, len(flat_data)):

        # checks to see if the index is 0 and if the value of flat_data at 0 is not equal to the next value
        if i == 0 and (flat_data[i] != flat_data[i + 1]):
            # if true add one to the count of repeats
            count_of_repeats += 1

        # checks to se if the last index is equal to the length of the flat_data and if the flat_data at the last index is equal to the second last index
        elif i == (len(flat_data)-1) and flat_data[i] != flat_data[i-1]:
            # if true add one to the count of repeats
            count_of_repeats += 1

        # checks to see if the next i is less than the value of the last index
        # checks if the flat-data at i is not equal before or after that i
        elif (i+1) < (len(flat_data) - 1) and flat_data[i] != flat_data[i - 1] and flat_data[i] != flat_data[i + 1]:
            # if true add one to the count of repeats
            count_of_repeats += 1

        # checks if the value of the flat_data at i is not in the updated_list
        # checks if the number of times that the value of flat_data at i is less than 15
        # because if it is greater than zero you have to start the count again
        elif flat_data[i] not in updated_list and flat_data.count(flat_data[i]) < 15:
            count_of_repeats += 1
            updated_list.append(flat_data[i])

        # checks if flat_data at i is not in the updated_list
        # checks if the number of times that the value of flat_data at i is greater than 15
        elif (flat_data[i] not in updated_list) and (flat_data.count(flat_data[i]) > 15):
            # sets the tracker to the number of times that the value of flat_data[i] appears
            tracker = flat_data.count(flat_data[i])
            # if the value of tracker is greater than 0
            while tracker > 15:
                # add one to the count of repeats
                count_of_repeats += 1
                # adds to the updated_list,
                # so it shows that the value has been checked already
                updated_list.append(flat_data[i])
                # subtracts 15 from the value of tracker
                tracker -= 15
                # goes back to the top of the loop
                continue
            while 0 < tracker < 15:
                # adds one to the number of repeats
                count_of_repeats += 1
                # adds to the updated_list,
                # so it shows that the value has been checked already
                updated_list.append(flat_data[i])
                # sets tracker to zero to exit the loop
                tracker = 0
    # returns the number of repeats
    return count_of_repeats

# encodes the rle data from the raw data that is passed in
# returns a RLE representation
def encode_rle(flat_data):
    # the encode_list
    encode_list = []

    # iterates over the range of 0 to the length of flat_data
    for i in range(0, len(flat_data)):

        # checks to see if the first index is 0
        # checks to see if the value one index ahead is not equal to the current flat_data
        if i == 0 and flat_data[i+1] != flat_data[i]:
            # if true add 1 to the encode_list
            encode_list.append(1)
            # append the value of flat_data at index 0
            encode_list.append(flat_data[i])

        # checks to see if index plus one is less than the length of the flat_data
        # checks to see if the flat_data is not equal to flat_data one before and one after
        elif (i+1) < len(flat_data) and flat_data[i] != flat_data[i-1] and flat_data[i] != flat_data[i+1]:
            # if true add 1 to the encode_list
            encode_list.append(1)
            # appends the value of the flat_data at the index
            encode_list.append(flat_data[i])

        # if i is the last index and the last index is not equal to one previous of the last index of flat_data
        elif i == (len(flat_data) - 1) and flat_data[i] != flat_data[i-1]:
            # if true add 1 to the encode_list
            encode_list.append(1)
            # appends the value of the flat_data at the index
            encode_list.append(flat_data[i])

        # if flat_data is not in the encode_list from 1 for every 2 indexs
        # and if the number of times flat_data[i] is less than 15
        elif flat_data[i] not in encode_list[1::2] and flat_data.count(flat_data[i]) < 15:
            # adds the number of times flat_data.count() appears
            encode_list.append(flat_data.count(flat_data[i]))
            # than adds the value of flat_data at i
            encode_list.append(flat_data[i])

        # if flat_data is not in the encode_list from 1 for every 2 indexs
        # and if the number of times flat_data[i] is greater than 15
        elif flat_data[i] not in encode_list[1::2] and flat_data.count(flat_data[i]) > 15:
            # sets the tracker to be zero
            tracker = flat_data.count(flat_data[i])
            # if the number of times flat_data appears is greater than 15
            while tracker > 15:
                # adds 15 to the encode_list
                encode_list.append(15)
                # adds the value of flat_data at i
                encode_list.append(flat_data[i])
                # subtracts 15 from the tracker exiting the loop
                tracker -= 15
                # going to the top loop
                continue
            # if the tracker is less than 15 and greater than 0
            while 0 < tracker < 15:
                # adds the number of trackers to the encode_list
                encode_list.append(tracker)
                # adds the value of flat_data at i
                encode_list.append(flat_data[i])
                # sets tracker to 0 exiting the loop
                tracker = 0

    # returns a encode list of the raw data
    return encode_list

# does the opposite of the encode_rle
# returns a decoded data set
def decode_rle(rle_data):
    num_list = []

    # goes through the rle data
    # skips over every  two takes the even indexs
    for i in range(0, len(rle_data), 2):
        # goes over the rle_data at the i
        for j in range(rle_data[i]):
            # adds that value plus one to the num_list
            num_list.append(rle_data[i+1])

    # returns the num_list
    return num_list

# returns the decompressed size RLE data used
# used to generate flat data
def get_decoded_length(rle_data):
    # the length of the data was the even index
    sum_even = 0

    # iterates over the rle_data by 2
    # this adds the value of the number of times that number is printed to the sum_even
    for i in range(0, len(rle_data), 2):
        sum_even += rle_data[i]

    return sum_even


# translates decimal to hex
# works like a key from decimal to hex
def hex_char_decode(digit):
    if digit == 0:
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

# does the reverse of hex_c
def hex_char_decode_rev(digit):
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
    elif digit == "a":
        return 10
    elif digit == "b":
        return 11
    elif digit == "c":
        return 12
    elif digit == "d":
        return 13
    elif digit == 'e':
        return 14
    elif digit == 'f':
        return 15

# does the opposite of to_hex_string
# goes from hexadecimal to byte data (decimal)
def string_to_data(data_string):
    # sets the initally values
    new_val_list = []

    # goes through data string
    # appends the value of the conversion of the hex to decimal value to new_val
    for i in data_string:
        new_val_list.append(hex_char_decode_rev(i))

    # returns the new_val_list
    return (new_val_list)

# goes from byte data to hexadecimal string
# returns this value
def to_hex_string(data):
    # new string
    total_sum = ""

    # iterates for every value in data
    for d in data:
        # converts the byte data to a hex string
        total_sum += str(hex_char_decode(d))

    # returns that new string
    return total_sum

# loads the image
def load_test_image():
    ConsoleGfx.test_image
    print("Test image data loaded.")

# translates RLE data into a human-readable rep
def to_rle_string(rle_data):
    # empty string
    new_string = ""

    # loops over the rle_data
    for element in range(0, len(rle_data)):
        # if the element is even
        # add the string value to the new string
        if element % 2 == 0:
            new_string += str(rle_data[element])

        # if the element is odd
        # add the hex character decoded from the rle element
        # adds a : at the end
        elif element % 2 == 1:
            new_string += str(hex_char_decode(rle_data[element])) + ":"

    # returns the new string minus the last term
    return new_string[:-1]

# translates a string in human-readable RLE format into RLE byte data
def string_to_rle(rle_string):
    # splits the rle_string from
    data = rle_string.split(":")
    # creates a new list
    new_list = []

    # iterates over the data
    for element in data:
        # sets the first byte
        first_byte = str(element[0:-1])
        # sets the last_byte
        last_byte = element[-1]

        # adds this to the new list for the first term
        new_list.append(int(first_byte))
        # adds this to the new list for the second term
        new_list.append((hex_char_decode_rev(str((last_byte)))))

    return new_list

def main():
    # sets the menu_option to be 0
    menu_option = 0

    # sets the image_data to be equal to 0
    image_data = None

    run_time = True
    # main loop
    while run_time:

        # runs the function that prints menu
        rle_menu()

        # stores the value of the menu
        menu_option = (input("Select a Menu Option: "))

        if menu_option == '0':
            run_time = False

        # loads the file to the program
        elif menu_option == '1':
            # asks user for the file name
            file_name = input("Enter name of file to load: ")
            # sets image_data to be the loaded image
            image_data = ConsoleGfx.load_file(file_name)

        # loads the test image
        elif menu_option == '2':
            load_test_image()

        # reads RLE String
        elif menu_option == '3':
            rle_val = input("Enter an RLE string to be decoded: ")
            image_data = decode_rle(string_to_rle(rle_val))

        # reads RLE Hex String
        elif menu_option == '4':
            hex_val = input("Enter the hex string holding RLE data: ")
            image_data = decode_rle(string_to_data(hex_val))

        # reads data hex string
        elif menu_option == '5':
            hex_val = input("Enter the hex string holding flat data: ")
            image_data = string_to_data(hex_val)

        # displays an image
        elif menu_option == "6":
            # if the image_data is None
            if image_data is None:
                print("Displaying image...")
            else:
                ConsoleGfx.display_image(image_data)

        # display RLE string
        elif menu_option == '7':
            # if the image_data is None
            if image_data is None:
                print("RLE Representation: (no data)")
            else:
                print("RLE representation:", to_rle_string(encode_rle(image_data)))

        # display hex rle data
        elif menu_option == '8':
            # if the image_data is None
            if image_data is None:
                print("RLE Representation: (no data)")
            else:
                print("RLE hex values:", to_hex_string(encode_rle(image_data)))

        # display hex flat data
        elif menu_option == '9':
            # if the image_data is None
            if image_data is None:
                print("Flat hex values: (no data)")
            else:
                print("Flat hex values:", to_hex_string(image_data))

        else:
            print("Error! Invalid input.")


if __name__ == '__main__':
    main()