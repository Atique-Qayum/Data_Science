
# data taype is string
# its a list
food = ["briyani", "kabab", "nehari", "halwa", "daal", "samosay"]
# indexing 0           1       2       3         4         5
print(food)

print(food[0])
print(food[-1])   # you can not put - sign wtih zero 0, so its start with -1

food[0] = "puloo" # update the value
print(food[0])

# its a tuples

coodinates = (4.21, 9.29)
print(coodinates)
print(coodinates[0])

# it a set
fruit_set = {"apple", "mango", "orange", "peach", "barry"}
print(fruit_set)
fruit_set.add("banana")
print(fruit_set)

# it a dictionary
car = {"brand": "toyota", "model":"corolla", "year":2022}
print(car)

print(car["brand"])   # enter key to print value

car["year"] = 2024
print(car)

#               order       Mutablity & Duplicate Items                       Access
# list          yes         yes & yes                                          Index  
# Tuple         yes         No & yes                                           Index
# set           no          Yes & no                                           N/A  
# Dictionary    yes         yes & yes(values only), No(keys must be unique)    key  