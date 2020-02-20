while True:
    x = int(input("Enter the number : "))
    if x>0 and x%2==0:
        print('The number is even positive')
    elif x<0 and x%2==0:
        print('The number is even negative')
    elif x>0 and x%2==1:
        print('The number is odd positive')
    elif x<0 and x%2==1:
        print('The number is odd negative')
    else:
        print('neither +VE nor -VE')
