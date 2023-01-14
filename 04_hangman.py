import random

# List of words to be used in the game
words = ["python", "programming", "language", "computer", "science"]

# Randomly select a word from the list
word = random.choice(words)

# Initialize the game variables
guessed_letters = []
attempts = 6

# Start the game loop
while attempts > 0:
    # Create a string with the correctly guessed letters
    current_word = ""
    for letter in word: 
        if letter in guessed_letters:
            current_word += letter
        else:
            current_word += "_"
    # Print the current word and the number of attempts left
    print("Word:", current_word)
    print("Attempts left:", attempts)
    
    # Get the player's guess
    guess = input("Guess a letter: ")
    
    # Check if the guess is valid
    if guess in guessed_letters:
        print("You have already guessed that letter. Try again.")
    elif guess in word:
        guessed_letters.append(guess)
        print("Correct!")
    else:
        attempts -= 1
        print("Incorrect.")
    
    # Check if the player has won
    if "_" not in current_word:
        print("Congratulations! You have won!")
        break

# Check if the player has lost
if attempts == 0:
    print("Sorry, you have lost. The word was", word + ".")
