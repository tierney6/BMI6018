#### File containing code for Assigment 5: Advanced Functions and Logic



# Question 3:
# Write a python program that, given an input list, will filter the input above a user defined threshold.
# This is to be done with a standard function.

# That is, given a list [1,2,3,4,5,6,7,8,9], and an argument (6), it should return [1,2,3,4,5,6]


# create a user defined function with name fun_three and two inputs: input_list and threshold
def fun_three(input_list, threshold):
    # first use an if else statement to ensure that the input_list is of type list, otherwise return error below
    if isinstance(input_list, list): 
        # second, use an if else statement to ensure that the threshold input is numeric, otherwise return error below
        if isinstance(threshold, (int, float)):
            # if both above criteria are met: use list comprehension to return an output list with only values below the input threshold
            output_list = [x for x in input_list if x <= threshold]
        else:
            print("Error: User defined input # 2: threshold input must be numeric")
    else: 
        print("Error: User defined input # 1: input_list is not a list")
    return(output_list)


# test on a given list and threshold
input_list = [0,1,2,3,4,5,6,7,8,9]
threshold = 6

fun_three(input_list, threshold)