counter = 0
while counter < 10:
    print("Hello world " + str(counter))
    counter += 1




sent_val = 'continue'
counter = 0
sum_user_input = 0
while sent_val not in ['quit', 'q', 'exit', 'stop']:
    counter += 1
    print("You are still in the loop!")
    print("you have been in the loop " + str(counter) + " times.")
    sent_val = input('Type quit to exit: ').lower()
    try:
        sum_user_input += int(sent_val)
        print("Current sum is: " + str(sum_user_input) + ".")
    except:
        print("User did not input an integer")
print("Your final sum after " + str(counter) + " attempts was: " + str(sum_user_input))
