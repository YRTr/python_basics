#Print the largest among three numbers
a = input("Enter the value of a : ")
A = int(a)
b = input("Enter the value of b : ")
B = int(b)
c = input("Enter the value of c : ")
C = int(c)
print("\n")
if A>B and A>C:
    print("The 1st largest value is : %d" %A)
    if B>C:
        print("\nThe 2nd largest value is : %d" %B)
        print("\nThe 3rd largest value is : %d" %C)
    else:
        print("\nThe 2nd largest value is : %d" %C)
        print("\nThe 3rd largest value is : %d" %B)
elif B>A and B>C:
    print("The 1st largest value is : %d" %B)
    if A>C:
        print("\nThe 2nd largest value is : %d" %A)
        print("\nThe 3rd largest value is : %d" %C)
    else:
        print("\nThe 2nd largest value is : %d" %C)
        print("\nThe 3rd largest value is : %d" %A)
elif C>A and C>B:
    print("The 1st largest value is : %d" %C)
    if A>B:
        print("\nThe 2nd largest value is : %d" %A)
        print("\nThe 3rd largest value is : %d" %B)
    else:
        print("\nThe 2nd largest value is : %d" %B)
        print("\nThe 3rd largest value is : %d" %C)
else:
    print("Any of the two numbers are equal")
