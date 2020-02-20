num=input("enter the number: ")
try:
    n=int(num)
except:
    print("Input must be a positive number")
rev=0
while n>0:
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
if int(num)==int(rev):
    print("The number {} equals its reverse {} :: Palindrome".format(num, rev))
else:
    print("The number {} not equals its reverse {} :: NOT palindrome".format(num, rev))
