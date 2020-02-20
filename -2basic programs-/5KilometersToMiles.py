K = input("Enter the number of kilometers")
try:
    kilometers = float(K)
except:
    print("Expected values")
Mile = (1.6)*(kilometers)
print("For a kilometers of %g -- The miles are : %g" %(kilometers, Mile))
