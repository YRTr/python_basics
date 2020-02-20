#Largest in the given list of numbers
largest = None
for var in [23,47,99,56,11]:
    if largest is None:
        largest = var
    elif var > largest:
        largest = var
    print("var : %d and Largest : %d" %(var, largest))
print("The largest of the numbers : %d", largest)
