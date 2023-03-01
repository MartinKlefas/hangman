# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

# Milestone 1
Set up the environment and linked it to the AiCore portal

# Milestone 2
Using the created repository create the variables for the game. Have the game randomly select a fruit from a hard coded list of fruits, and then have the user input a guess.
The script then simply checks if the guess is a single character and is in the alphabet (non-numeric etc)

# Milestone 3
Moved the code from milestone 2 into two functions:
1) check_guess - Checks if the guessed letter is in the hidden word
    - this accepts the guess as a string variable and prints the success/fail message to the stdout.
2) ask_for_input - accepts input from the user, validates that it's a single letter of the alphabet and then calls check_guess to see if it's in the hidden word.

# Milestone 4
Updated the functions from milestone 3 to include:
- warn about repeated letter guesses
- update the revealed portions of the word and the number of letters the user still needs to find
- track player lives
- changed the wording of the printed messages to reflect these changes

Added a basic test implementation of the class:
- create a short list of fruits
- manually added two letter guesses calls to test repeated input

# Milestone 5
created a function to oversee the game process
called function to run a game start-finish

#todo
- display game progress to user
- proper tests
- pull in larger word list from somewhere
- properly implement number of lives setting code
- draw the little hangman dude?