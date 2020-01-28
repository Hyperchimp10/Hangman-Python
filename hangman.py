import time
import random


def game():
    name = input("What is your name? ")
    print("Hello," +name+", play hangman")

    time.sleep(1)

    print("Start guessing...make sure you only guess in lowercase")

    time.sleep(0.5)
    words=["hangman", "chairs", "backpack", "bodywash", "clothing","computer", "python", "program", "glasses", "sweatshirt", "sweatpants", "mattress", "friends", "clocks", "biology", "algebra", "knives", "ninjas", "shampoo",'program', 'script', 'python', 'list', 'slice', 'data','turtle', 'dictionaries', 'string','loop','function','idle','import','print','while','index','return']
    guesses = ''
    turns = 0
    word=random.choice(words)

    print(words)


    while(turns <= 7):

        failed = 0
        for i in word:
            if i in guesses:
                print(i)
            else:
                print("_\n",)
                failed += 1


        if failed == 0:
            print("You won")
            break



        guess = input("guess a character:")
        guesses += guess



        if guess not in word:
            turns= turns+1


        if (turns == 1):
            print("_________")
            print( "|	 |")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|________")

        elif (turns == 2):
            print( "_________")
            print( "|	 |")
            print( "|	 O")
            print( "|")
            print( "|")
            print( "|")
            print( "|________")

        elif (turns == 3):
            print( "_________")
            print( "|	 |")
            print( "|	 O")
            print( "|	 |")
            print( "|	 |")
            print( "|")
            print( "|________")

        elif (turns == 4):
            print ("_________")
            print ("|	 |")
            print ("|	 O")
            print ("|	\|")
            print ("|	 |")
            print ("|")
            print ("|________")

        elif (turns == 5):
            print ("_________")
            print ("|	 |")
            print ("|	 O")
            print ("|	\|/")
            print ("|	 |")
            print ("|")
            print ("|________")

        elif (turns == 6):
            print("_________")
            print("|	 |")
            print("|	 O")
            print("|	\|/")
            print("|	 |")
            print("|	/  ")
            print("|________")

        elif (turns == 7):
            print("_________")
            print("|	 |")
            print("|	 O")
            print ("|	\|/")
            print('|     |')
            print("|	/ \ ")
            print("|________")

        if turns == 7:
            print ("\nYou Loose")
            print( "\nThe word was: \n" + word)
            print('\nto play again write game()')
        
game()
