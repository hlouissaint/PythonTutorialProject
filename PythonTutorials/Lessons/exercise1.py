import datetime

def calculate_date(my_age):
    year = datetime.date.today().year
    return (100 - int(my_age)) + year

print("The purpose of the game is you tell you the year that you will turn 100 based on the age info provided")

fname = input("What is your first name: ")
lname = input("What is your last name: ")
age = input("What is your age: ")
target_age = calculate_date(age)

for i in range(target_age):
    print ("You will turn 100 in year: ", target_age)

