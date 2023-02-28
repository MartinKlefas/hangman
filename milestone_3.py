import random
import re

word_list = ["Apple","Banana","Pear","Orange","Plum"]

word = random.choice(word_list)

while True:
    guess = input("Please guess a single letter")

    try:
        if len(guess) == 1 and guess.isalpha():  #re.search([a-zA-Z],guess) :
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    except:
        print("Invalid letter. Please, enter a single alphabetical character.")

if guess in word:
    print("Good guess! %s is in the word.", guess)
else:
    print("Sorry, %s is not in the wordT Try again.", guess)
