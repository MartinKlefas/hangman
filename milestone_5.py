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
            
            counter = 0
            for letter in self.word:
                if letter.lower() == thisGuess:
                    self.word_guessed[counter] = thisGuess
                
                counter +=1
            
            self.num_letters -= 1
            print(self.word_guessed)
        else:
            print("Sorry, %s is not in the word." % thisGuess)
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
    

                
def play_game(word_list: list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            break


        

    
    
Fruits = ["Apple","Banana","Pear","Orange","Plum"]
game = play_game(Fruits)

