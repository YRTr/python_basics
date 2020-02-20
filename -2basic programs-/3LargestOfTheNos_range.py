x = int(input("How many numbers : "))
print("Enter the numbers : ")
mylist = []
for i in range(1,x+1):
    n = int(input())
    mylist.append(n)
largest = None
for val in mylist:
    if largest is None:
        largest = val
    elif val>largest:
        largest = val
print(f'The largest of the given numbers : {largest}')
