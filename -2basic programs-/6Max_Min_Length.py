#Without any built-in functions
t = int(input("Range of numbers : "))
lst=[]
for i in range(t):
    e = input("--> ")
    try:
        ele = int(e)
    except:
        print("wrong input")
    lst.append(ele)
print(lst)
largest = None
for iter in lst:
    if largest is None or largest<iter:
        largest = iter
    else:
        pass
print("Maximum of the list: {}".format(largest))
smallest = None
for iter in lst:
    if smallest is None or smallest>iter:
        smallest = iter
    else:
        pass
print("Minimum of the list: {}".format(smallest))
count=0
for c in lst:
    count+=1
print("The length of the list: {}".format(count))
