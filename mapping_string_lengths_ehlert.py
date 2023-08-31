"""
Program Name: mapping_string_lengths_ehlert.py
Author: Tony Ehlert
Date: 8/31/2023

Program Description: This program creates a list variable containing 10 different strings and also contains a
function to determine the length of each string.  Finally, this program maps the list to the function and then prints
out the length of each string to the console
"""


def len_of_string(input_string):
    """
    This method calculates the length of a provided string. Then creates a list containing the provided string, followed
    by the length of the string.  Lastly the newly created list is returned
    :param input_string: string to get length of
    :return: list containing the input string and the string's length
    """
    return_list = [input_string, len(input_string)]
    return return_list


# create a list of strings that is at least ten strings long
list_of_strings = ["A", "list", "of", "strings", "that", "is", "at", "least", "ten", "items", "long"]

# use the map function to map the list of strings to the function and covert it to a list of lists
list_of_lists = list(map(len_of_string, list_of_strings))

# output the length of each string (can use a for loop for to output this information)
for item in list_of_lists:
    print(str(item[1]), end=', ')
