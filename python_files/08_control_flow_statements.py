# conditional statements
# < , > , == , != , >= , <=

x = 11
if x > 0:
    print("X is positive")
elif x < 0:
    print("X is negative")
else:
    print("X is ZERO")


# for loops
    
menu = ["briyani", "kabab", "nehari", "halwa", "daal", "samosay"]

for food in menu:
    print(food)


# while loops

i = 1
while i < 6:
    print(i)
    i += 1


# control statement

for letters in "python":
    if letters == "h":
        break
    print(letters)

for letters in "python":
    if letters == "h":
        continue
    print(letters)

for letters in "python":
    if letters == "h":
        pass
    print(letters)

