import random
import math

def check(ran, y):
    if(y>ran):
        print('Your guess is too low.')
    else:
        print('Your guess is too high.')
    count=1
    while(y!=ran):
        print('take a guess')
        y=int(input())
        if(y>ran):
            print('Your guess is too low.')
        else:
            print('Your guess is too high.')
        count+=1
    return count
    


print("Hello! What is your name?")
name=input()

lower = int(input("Enter Lower bound:- "))

upper = int(input("Enter Upper bound:- "))

print ("Well,", name, ", I am thinking of a number between", lower ,"and", upper)


x = random.randint(lower, upper)
y= int(input())


count = check(x,y)
print('Good job',name,'!' ' ' 'Your guessed my number in',count,'guesses')
