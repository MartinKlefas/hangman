import random
word_list = ["Apple","Banana","Pear","Orange","Plum"]

word = random.choice(word_list)
print(word)

guess = input("Please guess a single letter")

try:
    if len(guess) == 1 :
        print("Good Guess")
    else:
        print("Oops! that is not a valid input")
except:
    print("Oops! that is not a valid input")