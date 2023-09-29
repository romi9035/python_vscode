# Step 4

import random
import hangman_art
import hangman_words
import os
stages = hangman_art.stages

end_of_game = False
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.
lives = 6
# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)
# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
guess_letter = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system('cls')
    match = False
# TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in guess_letter:
        print(f"You have already guessed this letter {guess_letter}")
    else:
        guess_letter.append(guess)
        # Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess:
                display[position] = letter
                match = True

        # TODO-2: - If guess is not a letter in the chosen_word,
        # Then reduce 'lives' by 1.
        # If lives goes down to 0 then the game should stop and it should print "You lose."
        if match == False:
            # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
            print(
                f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
        # Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

        # Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You win.")
        elif lives == 0:
            end_of_game = True
            print("You lose.")

        # TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])
