# Welcome to my Guessing Game

#blueprint
# get an array of possible names, at the beginning of the game iterate through this array and pic a random Name
# This random name is now the secret word. 
# ask the player to pick a guess from a suggestion of options. 
# the player has 3 trials to get the correct name
# this name should match the secret random word you picked when you iterated through the array from the array 

#Greetings
print('HOW TO PLAY:\nchoose a name from the options provided\nYou have 3 trials to match the words\nGood Luck!!!\n\n')


#import modules and declare necessary variables
import random
words = ['nweke','nwafor','nworie','nwankwo','eke','orie','afor','nkwo']
secret_word = random.choice(words).upper()
trial_count = 2
trial = 0

#processes
print("Here are your Choices: \n'nweke','nwafor','nworie','nwankwo','eke','orie','afor','nkwo'")
while trial_count >= trial:
    choice = input("choose a name from the choice list:" )
    if choice == secret_word and trial_count <= trial:
        print(f'CONGRATULATIONS YOUR GUESS WAS RIGHT\nTHE SECRET WORD WAS {secret_word}')
    elif trial_count == 0:
        print(f'GAME OVER!! you are out of trials')
        break
    else:
        print(f'Sorry your guess {choice} was wrong\nYou have {trial_count} tries left\nTRY AGAIN')
        trial_count -= 1



#At the end of the game, display the secret word
print(f'The secret word was {secret_word}!!')

