X=(input("Enter the number: ")
try:
    x=int(X)
except:
    print("Accepts only integers. Try again.")
a=1
fact=1
while a<=x:
    fact=fact*a
    a+=1
print("The factorial : {}".format(fact))
