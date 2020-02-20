x=int(input("enter the number: "))
rev=0
while x>0:
    rem=x%10
    rev=(rev*10)+rem
    x=x//10
print("The reverse of the given number : {}".format(rev))
