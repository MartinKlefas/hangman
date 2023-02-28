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

         self.word_guesses = underscore_list
         
