"""
Abigail Boggs
amboggs@dmacc.edu
9/20/23

This program is a basic for loop program
"""


# This for loop goes through the floats in the list
floating_point_nums = [0.12, 0.543, 12.5, 99.90, 50.4213]

for index_of_num in floating_point_nums:
    print(str(index_of_num))

# this loop prints the odd numbers between 99 to 33
nums_descending = range(100,32,-1)

for index in nums_descending:
    if index % 2 == 1:
        print(str(index), end=", ")
