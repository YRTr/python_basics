a = int(input('Enter the number : '))
count = 0
print("The factors of the number {}".format(a))
for i in range(1,a+1):
    if a%i==0:
        print(i)
        count+=1
print("Total number of factors : {}".format(count))
print("Number of factors without 1 and {} : {}".format(a, count-2))
