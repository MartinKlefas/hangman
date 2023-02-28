# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

# Milestone 1
Set up the environment and linked it to the AiCore portal

# Milestone 2
Using the created repository create the variables for the game. Have the game randomly select a fruit from a hard coded list of fruits, and then have the user input a guess.
The script then simply checks if the guess is a single character and is in the alphabet (non-numeric etc)

# Milestone 3
Moved the code into two functions:
1) check_guess - Checks if the guessed letter is in the hidden word
2) ask_for_input - accepts input from the user, validates that it's a single letter of the alphabet and then calls check_guess to see if it's in the hidden word.

