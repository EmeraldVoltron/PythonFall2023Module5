"""
Abigail Boggs
amboggs@dmacc.edu
9/20/23

This program is to demonstrate input validation with a while loop
"""

num_list = []
user_in = ""

sentinel_value = 'continue'
while sentinel_value != 'quit':
    user_in = input("Enter a number between 1 and 100, or 'quit' to quit: ")
    if user_in.lower() != 'quit':
        while float(user_in) >= 100 or float(user_in) <= 1:
            user_in = float(input("Try again, enter a number between 1 and 100: "))
        num_list.append(float(user_in))
    else:
        sentinel_value = 'quit'

#print list
print(num_list)

# TESTS:

# TEST 1:
# inputs: 1, 2, 3, 4, 5, 6, 7, 8, quit
# expected output: when 1 is entered it should be reprompted to enter a new number, enter 12
# list should only contain [12, 2, 3, 4, 5, 6, 7, 8]
# actual output: [12.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]

# TEST 2:
# inputs: 101 (reprompted: 11), 2, 3 , 4, 5, 123 (reprompted: 12), quit
# excepted output: 11, 2, 3, 4, 5, 12
# actual output: [11.0, 2.0, 3.0, 4.0, 5.0, 12.0]