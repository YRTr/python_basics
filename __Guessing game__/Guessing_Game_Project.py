import random
print('---GAME RULES AND INSTRUCTIONS---')
print("Guess a random integer from 1 to 100")
print("The rules are........")
print("If a player's guess is \n_less than lowest number range_or_greater than greatest number range_:: say 'OUT OF BOUNDS'")
print("1.If player's guess is 'greater than 20 of random' : return _A long Way_")
print("2.If player's guess is 'diff with 11 and 20(both include) of random&guess' :\n\treturn _Not close_")
print("3.If player's guess is 'diff within 6 and 10(both include) of random&guess' :\n\treturn _Almost_")
print("4.If player's guess is 'diff within 3 and 5(both include) of random&guess :\n\treturn _Warmer_'")
print("5.If player's guess is 'diff within 2 and 1(both include) of random&guess:\n\treturn _Thats very close_'")
print("6.If player's guess equals the random number: _Congratulate and break_")
print("\n\n")
print("___________LET's PLAY__________")
startr=int(input("Enter the starting range: "))
endr=int(input("Enter the ending range: "))
guesses=[0]
count=0
while True:
    r=random.randint(startr,endr)
    guess=int(input("Guess the number! "))
    count+=1
    if guess<startr or guess>endr:
        print("Out of the bounds")
    elif abs(guess-r)>20:
        print('A long way')
    elif abs(guess-r)>10 and abs(guess-r)<21:
        print('Not close')
    elif abs(guess-r)>5 and abs(guess-r)<11:
        print("Almost")
    elif abs(guess-r)>2 and abs(guess-r)<=5:
        print("Warmer")
    elif abs(guess-r)<=2 and abs(guess-r)>=1:
        print("That's very close")
    elif guess == r:
        print("Guess is correct. WINNER!. You guessed the game in {} !Guesses!".format(len(guesses)))
        break
    guesses.append(count)
