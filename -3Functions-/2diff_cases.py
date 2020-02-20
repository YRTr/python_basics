def case(string):
    '''
    Python function that accepts a string and calculates the number
    of upper case letters and lower case letters.
    '''
    ucount = 0
    lcount = 0
    punc = 0
    for char in range(0,len(string)-1):
        if string[char].isupper():
            ucount += 1
        elif string[char].islower():
            lcount += 1
        else:
            punc += 1
    print('Number of upper case letters: {}'.format(ucount))
    print('Number of lower case letters: {}'.format(lcount))
    print('Number of punctuation: {}'.format(punc))
