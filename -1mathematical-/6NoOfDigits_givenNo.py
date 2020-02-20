X=input("Enter the number: ")
x=int(X)
count=0
dig=0
while x>0:
    num=x%10
    dig=dig*10+num
    count+=1
    x=x//10
print("The number of digits in given number {} : {}".format(X,count))
