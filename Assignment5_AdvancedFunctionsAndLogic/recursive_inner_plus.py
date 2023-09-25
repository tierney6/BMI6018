
### File containing code for Assigment 5: Advanced Functions and Logic

# Question 2:
#  Write the a python program that, given an input list of any level of complexity/nestedness, will return the inner most list plus 1. 
# This is to be done with recursion. 
# Note: the input will contain only integers or lists. 

# This is the same but now with recursion instead of a while loop
# Name the function fun_two and give it input
def fun_two(input_list):
    # use a nested if else statement
    # if item is a list
    if isinstance(input_list, list):
        if not input_list:
            return input_list
        # if the input_list is of type list, create a new list isList_bool that uses list comprehension to create a True False list
    # every item in the input_list that is a list returns True, otherwise returns False
        isList_bool = [type(x) == list for x in input_list]
        # if there is at least one list that is an item in input_list, i.e. if input_list is a nested list then rerun the function on the subset of the original list that is itself a list
        if True in isList_bool:
            return fun_two(input_list[isList_bool.index(True)])
        # otherwise, if there are no more lists within the input_list, then add 1 to each of the items in the list
        else:
            return [x + 1 for x in input_list]
    # otherwise if remaining item is an integer only, return the integer + 1
    elif isinstance(input_list, int):
        return input_list + 1
    else:
        return input_list

# Test the function with a nested list
input_list = [1, 2, 3, 4, [5, 6, 7, [8, 9]]]
result = fun_two(input_list)
print("Innermost list plus 1:", result)