import random
import time

number=random.randint(1 ,100)
def intro():
    print('may i ask you for yor name')

    global name
    name=input()
    print(name+'we are going to play a game . i am thinkigof a number')
    if(number%2==0):
        x='even'
    else:
        x='odd'
    print('\nThis is an {}number'.format(x))
    time.sleep(.5)
    print('Go ahead. Guess:')
def pick():
    gussesTaken = 0
    while guessesTaken<6:
     time.sleep(.25)
     enter=input('Guess:')


    try:
       guess =int(enter)

       if guess<=100 and guess>=1:
        guessestaken=guessestaken+1
        if guessesTaken<6:
                if guess<number:
                  print('the guess of the number that you have enterred is too low')
                if guess > number:
                    print('the guess of the number that you have enterred is too high')
                if guess != number:
                 time.sleep(.25)
                 print('tryagain')

                if guess==number:
               
                        break
       if guess>100  or guess<1:
             print('silly goose!that umber in tin the range!')
             time.sleep(.25)
    except:
       print('i dont think that')
    if guess == number:
        guessesTaken =str(guessestaken)

intro()
pick()
print('do you want to play again ')
playagain=input()