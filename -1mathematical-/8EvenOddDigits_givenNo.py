num=input("Enter the number: ")
try:
    n=int(num)
except:
    print("Acceptable: only positive integers")
ec=0
oc=0
while n>0:
    rem=n%10
    if rem%2==0:
        print("The number {} is 'EVEN'".format(rem))
        ec+=1
    else:
        print("The number {} is 'ODD'".format(rem))
        oc+=1
    n=n//10
print("The even digits in given number {} : {}".format(num,ec))
print("The odd digits in given number {} : {}".format(num,oc))
