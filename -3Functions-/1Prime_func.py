def number(num):
    count = 0
    if num > 0:
        for a in range(1,num+1):
            if num%a == 0:
                count += 1
            else:
                pass
    else:
        print('Undefined')
    if count > 2:
        print('{} is a composite'.format(num))
    elif count == 1:
        print('{} is Neither a -prime- nor -composite-'.format(num))
    elif count == 2 and num == 2:
        print('{} is only Even prime number.'.format(num))
    elif count == 2 and num != 1 and num != 2:
        print('{} is a prime.'.format(num))
