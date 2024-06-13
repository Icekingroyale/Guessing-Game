# Welcome to my Guessing Game

# blueprint
# get an array of possible names, at the beginning of the game
# iterate through this array and pick a random name
# This random name is now the secret word.
# ask the player to pick a guess from a list of options.
# the player has 3 trials to get the correct name
# this name should match the secret random word you picked when you iterated through the array
# Ask the player if he wants to play again if yes, start afresh, if no end the game



import random
# Player greetings
print('HOW TO PLAY:\nchoose a name from the options provided\nYou have 3 trials to match the words\nGood Luck!!!')
print('----------------------------------------------------------------------------------------------')



# processes


def main_game():
    #declare necessary variables
    words = ['nweke', 'nwafor', 'nworie', 'nwankwo', 'eke', 'orie', 'afor', 'nkwo']
    secret_word = random.choice(words)
    trial_count = 2
    trial = 0

    print("Here are your Choices: \n'nweke','nwafor','nworie','nwankwo','eke','orie','afor','nkwo'")
    while trial_count >= trial:
        choice = str(input("choose a name from the choice list: "))
        

        if choice == secret_word and trial_count <= trial:
            print(f'CONGRATULATIONS YOUR GUESS WAS RIGHT\nTHE SECRET WORD WAS {secret_word}')
            
        elif trial_count == 0:
            print(f'GAME OVER!! you are out of trials')
            break                      
        else:
            print(f'Sorry your guess {choice.upper()} was wrong\nYou have {trial_count} tries left\nTRY AGAIN')
            print('____________________________________________________________________________')
            print("Here are your Choices: \n'nweke','nwafor','nworie','nwankwo','eke','orie','afor','nkwo'")
            trial_count -= 1
        # At the end of the game, display the secret word
    print(f'The secret word was {secret_word.upper()}!!')
            

main_game()        

#player deciding if he wants to play again or not
print('*************************************************************')
yes = 'yes'
no = 'no'
while True:
    x = str(input('Do you want to play again?: YES? NO?: '))
    if x == 'yes':
        main_game()
    elif x == 'no':
        print('Thank you for playing, have a nice day!')
        break
    else:
        print(f"{x} not a valid selection\nPick yes or no")

