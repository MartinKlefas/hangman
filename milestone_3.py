while True:
    guess = input("Please guess a single letter")

    try:
        if len(guess) == 1 and guess.isalpha():  #re.search([a-zA-Z],guess) :
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    except:
        print("Invalid letter. Please, enter a single alphabetical character.")