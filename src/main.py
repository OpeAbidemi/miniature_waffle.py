# User will have to guess the randomly generated word. You can create a list from which the word
# would have to be guessed and also set a cap on the number of guesses allowed.
# When the user inputs the word, you can indicate whether the alphabet written appears in this
# particular position or not. You will need a function to check if the user is inputting alphabets or
# numbers and to display error messages appropriately

import random

list_of_words = ['python', 'java', 'kotlin', 'javascript', 'c++', 'c#', 'c', 'php', 'ruby', 'perl', 'go']

levels = ["Beginner" ,"Moderate", "Expert"]

level = "Beginner"

# this function asks the user to choose a level and returns ir
def get_level():
    # Select the level
    print("Select the level:")
    print("1. Beginner - Max of 5 letter words")    
    print("2. Moderate - 6 - 8 letter words")
    print("3. Expert - above 8 letter words")

    choice = int(input("Enter the level: "))
    # Return level
    return list(levels)[choice-1]

# This function generates a random word
def get_random_word(level):
    resolved : list
    # filters the list according the level
    if level == "Beginner":
        resolved = random.choice(list(filter(lambda x: len(x) <= 5, list_of_words)))
    elif level == "Moderate":
        resolved = random.choice(list(filter(lambda x: len(x) > 5 and len(x) <= 8, list_of_words)))
    elif level == "Expert":
        resolved = random.choice(list(filter(lambda x: len(x) > 8, list_of_words)))

    return resolved

# This function gets the user guessed word
def get_user_input():
    return input('Enter your guess: ')

# This function starts the whole game
def play():
    while True:
        # Introduces the game
        print("Guess the word!\n")
        print("You will have to guess the randomly generated word from the words listed below.\n")

        for word in list_of_words:
            print(word)
        
        print("\n")

        # Checks if the user inputs an invalid level
        while True:
            try:
                level = get_level()
            except(IndexError):
                print("Invalid level, You can only select 1, 2 or 3")
                # ask the user input the level again
                continue;
            break;
        
        # Display the selected level
        print("You've selected level: " + str(level))
        
        random_word = get_random_word(level)
        guess = get_user_input()

        if random_word == guess:
            print("Yay, You guessed the word. The word is " + guess)
        else:
            print("Oops, Your guess is wrong. The word is " + random_word)

        print("Would you like to play again?")
        print("1.Yes \t\t 2.No")
        choice = int(input("Would you?:  "))
        if choice == 1:
            print("Starting the game again")
            continue;
        elif choice == 2:
            print("Exiting the game")
            exit()


# Start the game
play()

