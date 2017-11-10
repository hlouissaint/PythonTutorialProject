def get_list(numb):
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = []
    for i in a:
        if int(i) < int(numb):
            b.append(i)
    return b

token = int(input("Please enter a token value less then 100: ===> "))
small_list = get_list(token)
print ("The numbers that are less than 5 are as follow", small_list)