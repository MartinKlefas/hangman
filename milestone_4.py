import random

class Hangman:
    def __init__(self, word_list, num_lives = 5) -> None:
         self.word_list = word_list
         self.num_lives = num_lives
         self.word = random.choice(word_list)



         self.num_letters = len(set(self.word))
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
            underscore_list = list()

            for letter in self.word:
                if letter.lower() == thisGuess:
                    underscore_list.append(letter)
                else:
                    underscore_list.append("_")
            
            self.word_guessed = underscore_list
            self.num_letters -= 1
        else:
            print("Sorry, %s is not in the wordT Try again." % thisGuess)
            self.num_lives -= 1
            print("You have %s lives left." % self.num_lives)


    def ask_for_input(self):
        invalid_input = True
        while invalid_input:
            guess = input("Please guess a single letter: ")

            try:
                if not len(guess) == 1 or not guess.isalpha():  
                    print("Invalid letter. Please, enter a single alphabetical character.")
                elif guess in self.list_of_guesses:
                    print("You already tried that letter!")
                else:
                    self.check_guess(guess)
                    invalid_input = False
                
                self.list_of_guesses.append(guess)
                
                
            except:
                print("Exception. Please, enter a single alphabetical character.")

    
    
Fruits = ["Apple","Banana","Pear","Orange","Plum"]
new_game = Hangman(Fruits)
new_game.ask_for_input()
new_game.ask_for_input()
