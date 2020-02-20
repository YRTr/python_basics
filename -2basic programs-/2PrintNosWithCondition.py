#   Write a program that prints the integers from 1 to 100.
#   But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz".
#   For numbers which are multiples of both three and five print "FizzBuzz".
num1 = int(input("Starting number: "))
num2 = int(input("Ending number: "))
for numbers in range(num1,num2+1):
    if numbers%3==0 and numbers%5==0:
        print('FizzBuzz')
    elif numbers%3==0 and numbers%5!=0:
        print('Fizz')
    elif numbers%5==0 and numbers%3!=0:
        print('Buzz')
    else:
        print(numbers)
