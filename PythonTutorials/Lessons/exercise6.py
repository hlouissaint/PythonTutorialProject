while 1 == 1:
    val = input("Please enter a palindrome : ===>  ")
    rval = ''.join(reversed(val))

    if val == rval:
        print("The word you entered is a lalindrome")
    else:
        print ("Better luck next time")
