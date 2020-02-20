from random import randint
print('-----DICE ROLLING SIMULATOR-----')
print('The GOAL: Like the title suggests, this project involves\nwriting a program that simulates rolling dice.')
print('When the program runs, it will randomly choose the number\nbetween 1 and 6.(Or Whatever other integer you prefer -\nthe number of sides on the die is up to you)')
print('The program will print what that number is.\nHow many attempts to roll again.')
print("For this project, you'll need to set the min and max\nnumber that your dice can produce.\nFor the average die, that means a minumum 1 and maximum 6.")

p=input("Enter the total number of players(numeric): ")
player=int(p)
print('The names of the players in sequence: ')
lst=[]
while True:
    inp=input("> ")
    lst.append(inp)
    if len(lst)<player:
        continue
    else:
        break
print(lst)
for i,j in enumerate(lst):
    print('{} - {}'.format(i+1,j))
def dice1(x):
    ran1=randint(1,6)
    return ran1
def dice2(x):
    ran2=randint(1,6)
    return ran2
a=0
at=int(input("How many attempts you wish to play?: "))
while at>0:
    for a in range(1, player+1):
        print('player - {} ===>'.format(a))
        c=input('Choose x to role the dice: ')
        d1=int(dice1(c))
        d2=int(dice2(c))
        print('roll {},{}'.format(d1,d2))
        d=d1+d2
        print(d)
        a+=1
    at-=1
