# Problem3: printing out all available letters

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    result = string.ascii_lowercase[:28] # get all the char and store it 
    for item in lettersGuessed: # iterate i in the list lettersGuessed
        result = result.replace(item,'') # delete the letter in result
    return result
