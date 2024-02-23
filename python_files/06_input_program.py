# name = input("Enter your name:")   # user input

# print("Hello ", name, " hope you are doing well!")

person1 = input("Enter your name of first person:")
person2 = input("Enter your name of second person:")
age1 = input("Enter your person1 age:")
age2 = input("Enter your person2 age:")

if age1 > age2:
    print(person1, " is older than ", person2)
elif age1 < age2:
    print(person2, " is older than ", person1)
else:
    print("Both people are of same age.")
