def pig_latin(word):
    '''
    Pig Latin is a languafe game in which words in English are altered, usually by adding a fabricated suffix
    or by moving the onset or initial consonant or consonant cluster of a word to the end to the word and adding
    a vocalic syllable to create such a suffix.
    '''
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'O', 'I', 'U']
    if word[0] in vowels:
        return word[:] + 'ay'
    else:
        return word[1:] + word[0] + 'ay'
