x = int(input("Enter the number: "))
factc = []
count = 0
i=1
while i<x+1:
    if x%i == 0:
        factc.append(i)
        count+=1
    i+=1
print("The factors of given number : ")
print(factc)
print("The total number of factors : {}".format(count))
if count<3:
    print("The given number {} is a prime, factors 1 and itself({})".format(x, x))
if count>=3:
    print("The given number {} is a composite".format(x))
