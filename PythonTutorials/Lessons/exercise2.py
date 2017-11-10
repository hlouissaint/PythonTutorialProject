
print ("The purpose of this exercise is to determine wether the value provided is odd or even")
while True:
    numb = int(input("Please enter a number less than 100 ===> "))
    val = numb % 2
    if val == 0:
        print("The integer that you provided is even")
    else:
        print("The integer that you provided is odd")
