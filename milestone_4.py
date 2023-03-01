import random

class Hangman:
    def __init__(self, word_list, num_lives = 5) -> None:
         self.word_list = word_list
         self.num_lives = num_lives
         self.word = random.choice(word_list)
         self.num_letters = len(self.word)
         self.list_of_guesses = list()

         underscore_list = list()

         for letter in self.word:
            underscore_list.append("_")

         self.word_guessed = underscore_list

    #methods
    def check_guess(self,thisGuess):
        thisGuess = thisGuess.lower()
        if thisGuess in self.word.lower():
            print("Good guess! %s is in the word." % thisGuess)
        else:
            print("Sorry, %s is not in the wordT Try again." % thisGuess)

    def ask_for_input(self):
        while True:
            guess = input("Please guess a single letter: ")

            try:
                if not len(guess) == 1 or not guess.isalpha():  
                    print("Invalid letter. Please, enter a single alphabetical character.")
                elif guess in self.list_of_guesses:
                    print("You aleady tried that letter!")
                else:
                    self.check_guess(guess)
                
                self.list_of_guesses.add
                
            except:
                print("Invalid letter. Please, enter a single alphabetical character.")
    
Fruits = ["Apple","Banana","Pear","Orange","Plum"]
new_game = Hangman(Fruits)
new_game.check_guess("A")
