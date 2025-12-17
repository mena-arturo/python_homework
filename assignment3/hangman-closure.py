# -------- Task 4: Closure Practice --------------------------------------------------------------------------------
'''
	1. Within the assignment3 folder, create a file called hangman-closure.py.
	2. Declare a function called make_hangman() that has one argument called secret_word.
           It should also declare an empty array called guesses. Within the function declare a function
           called hangman_closure() that takes one argument, which should be a letter.
           Within the inner function,
           each time it is called, the letter should be appended to the guesses array.
           Then the word should be printed out, with underscores substituted for the letters
           that haven't been guessed.
           So, if secret_word is "alphabet", and guesses is ["a", "h"],
           then "a__ha__" should be printed out.
           The function should return True if all the letters have been guessed,
           and False otherwise. make_hangman() should return hangman_closure.
	3. Within hangman-closure.py, implement a hangman game that uses make_hangman().
           Use the input() function to prompt for the secret word.
           Then use the input() function to prompt for each of the guesses, until the full word is guessed.
	4. Test your program by playing a few games.
'''

def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        nonlocal guesses
        new_string = ""
        guesses.append(letter)
        for i in range(len(secret_word)):
            if (secret_word[i] in guesses):
                new_string += secret_word[i]
            else:
                new_string += "_"
        print ("You guessed: ", new_string)

        if "_" in new_string:
            return False
        else:
            return True

    return hangman_closure

            
def play_hangman():
    exit = False
    secret_word = input("Let's play hangman. Enter the secret word: ")
    game = make_hangman(secret_word)
    while not exit:
        letter = input("Enter a letter for your guess. (Game is case sensitive): ")
        exit = game(letter)

play_hangman()
