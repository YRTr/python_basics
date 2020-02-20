x = int(input("How many numbers : "))
print('Enter the numbers : ')
mylist = []
for i in range(1,x+1):
    num = int(input())
    mylist.append(num)
print(mylist)
#To find the largest of the numbers
largest = None
for i in mylist:
    if largest is None:
        largest = i
    elif i>largest:
        largest = i
print("The largest of the number : {}".format(largest))
#To find the smallest of the numbers
smallest = None
for i in mylist:
    if smallest is None:
        smallest = i
    elif i<smallest:
        smallest = i
print("The smallest of the number : {}".format(smallest))
