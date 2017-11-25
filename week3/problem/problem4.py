import string

def getAvailableLetters(lettersGuessed):
    result = string.ascii_lowercase[:28]
    for item in lettersGuessed:
        result = result.replace(item,'')
    return result

def isWordGuessed(secretWord, lettersGuessed):
    secretList = list(secretWord)
    i = 0

    while (i < len(secretList)):
        if (secretList[i] in lettersGuessed): # is True
            i += 1
        else:
            return False
            break
    return True

def getGuessedWord(secretWord, lettersGuessed):
    i = 0
    # string is immutable to make a new variable to collect letters as a string object
    result = ''
    while (i < len(secretWord)):
        if (secretWord[i] in lettersGuessed): # if it  exists
            result += secretWord[i] # add it to result
        else: # if it does not exit then add an underscore
            result += '_ '
        i += 1 # add + 1 so that it breaks once it iterates the word
    return result

def isIn(secretWord, user_guess):
    if (user_guess in secretWord):
        return True
    return False

# PROBLEM SOLVING USING FUCNTIONS THAT I HAVE CREATED

def hangman(secretWord):
    mistakeMade = 0
    lettersGuessed = []
    availableLetters = string.ascii_lowercase

    # INTRO
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ', len(secretWord), ' letters long')

    # ROUND
    while (mistakeMade < 8) and (not isWordGuessed(secretWord, lettersGuessed)):
        print('-----------')
        print('You have ' + str(8 - mistakeMade) + ' guesses left.')
        print('Available Letters : ', availableLetters)
        user_guess = input('please guess a letter: ') # ASK FOR AN INPUT GUESS
        lettersGuessed.append(user_guess)

        if (not user_guess in availableLetters): # LETTER HAS BEEN GUESSED
            print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))

        else: # LETTER HAS NOT BEEN GUESSED
            if (isIn(secretWord, user_guess)): # LETTER IS IN SECRETWORD
                print('Good guess: ', getGuessedWord(secretWord, lettersGuessed))

            else: # LETTER IS NOT IN SECRET
                print('Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
                mistakeMade += 1
        availableLetters = getAvailableLetters(lettersGuessed)

    print('-----------') # ONCE IT IS DONE
    if (isWordGuessed(secretWord, lettersGuessed)): # IF DONE BECAUSE THE WORD IS CORRECT
        print('Congratulations, you won!')
    else: # IF DONE BECAUSE MISTAKE > 8
        print('Sorry, you ran out of guesses. The word was else. ')
    return
