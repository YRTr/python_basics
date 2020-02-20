num=input("Enter any number: ")
try:
    n=int(num)
except:
    print("The input must be natural number only")
sum=0
while n>0:
    i=n%10
    sum=sum+i
    n=n//10
print("The sum of the digits of a number {} : {}".format(num,sum))
