# problem2 : create second function
# Next, implement the function getGuessedWord that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed. This function returns a string that is comprised of letters and underscores, based on what letters in lettersGuessed are in secretWord. This shouldn't be too different from isWordGuessed!


def getGuessedWord(secretWord, lettersGuessed):
    i = 0
    # string is immutable to make a new variable to collect letters as a string object
    result = ''
    while (i < len(secretWord)):
        if (secretWord[i] in lettersGuessed): # if it  exist
            result += secretWord[i] # add it to result
        else: # if it does not exit then add an underscore
            result += '_ '
        i += 1 # add + 1 so that it breaks once it iterates the word
    return result

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(secretWord, lettersGuessed))
# '_ pp_ e'
