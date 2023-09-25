
### File containing code for Assigment 5: Advanced Functions and Logic

### Question 1: Write a python program that, given an input list of any level of complexity/nestedness, will return the inner most list plus 1. 
### This is to be done with a while loop. Note: the input will contain only integers or lists. 

# As an example:

# input_list = [1,2,3,4,[5,6,7,[8,9]]]

# your_py_program.py input_list will produce: [9,10]

# That is [8, 9] (the inner most list) plus 1 -> [9, 10]

# name the function "fun_one" and give it a named input of "input_list"
def fun_one(input_list):
    # while the input_list is a list type object:
    while isinstance(input_list, list):
        # if it's not a list type object, break the while loop
        if not input_list:
            break
        # create an empty list to store boolean values in
        isList_bool = []
        # for all the items in the list, determine if the item is a list and store these as True False boolean items in isList_bool
        for i in range(len(input_list)):
            isList_bool.append(type(input_list[i]) == list)
        # if there is a True value in the isList_bool, overwrite the original input_list with just the ones with lists
        if True in isList_bool:
            input_list = input_list[isList_bool.index(True)]
        # if there are no True values, all of the items, the list is no longer nested and we can use this list as the output to add 1 to
        else:
            break
    # if the out put is an integer add 1 to it; if it's a list use list comprehension to add 1 to all the values
    return  input_list + 1 if isinstance(input_list, int) else [x + 1 for x in input_list]

# Test the function with a nested list
input_list = [1, 2, 3, 4, [5, 6, 7, [8, 9]]]
result = fun_one(input_list)
print("Innermost list plus 1:", result)
