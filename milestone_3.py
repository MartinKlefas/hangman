import random


def check_guess(guess):
    guess = guess.lower()
    if guess in word.lower():
        print("Good guess! %s is in the word." % guess)
    else:
        print("Sorry, %s is not in the wordT Try again." % guess)

def ask_for_input():
    while True:
        guess = input("Please guess a single letter: ")

        try:
            if len(guess) == 1 and guess.isalpha():  
                break
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")
        except:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)






word_list = ["Apple","Banana","Pear","Orange","Plum"]

word = random.choice(word_list)

ask_for_input()


