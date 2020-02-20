x = int(input("Enter the range number : "))
a = 0
b = 1
print('Fibonacci series with in range 1 to {}'.format(x))
print(a)
print(b)
for i in range(1,x):
    c = a+b
    print(c)
    a = b
    b = c
