import random


a=[1,2,3,4,5,6,7,8,9,10]

x=int(input('Enter a value between 1 to 10 '))

y= random.choice(a)

if x==y:
    print ('you win :)')
else :
    print ('You lose :(')
