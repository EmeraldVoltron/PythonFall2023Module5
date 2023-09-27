"""
Abigail Boggs
amboggs@dmacc.edu
9/20/23

This program is to demonstrate input validation with a while loop that has a break
"""

num_list = []
user_in = ""

sentinel_value = 'continue'
while sentinel_value != 'quit':
    user_in = input("Enter a number between 1 and 100, or 'quit' to quit: ")
    if user_in.lower() != 'quit':
        while float(user_in) >= 100 or float(user_in) <= 1:
            user_in = input("Try again, enter a number between 1 and 100: ")
            if user_in.lower() == 'quit':
                sentinel_value = 'quit'
                break
        else:
            num_list.append(float(user_in))
    else:
        sentinel_value = 'quit'

#print list
print(num_list)

# TESTS:

# TEST 1:
# inputs: 1 (reprompted 11), 2, 3, 4, 505 (reprompted: quit)
# expected output:
# list should only contain [11, 2, 3, 4]
# actual output: [11.0, 2.0, 3.0, 4.0]

# TEST 2:
# inputs: 11, 101 (reprompted: quit)
# excepted output: [11.0]
# actual output: [11.0]