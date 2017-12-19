import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object

        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class

        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.

        You may find the helper function is_word(wordlist, word) and the string method split() useful. Note that is_word will ignore punctuation and other special characters when considering whether a word is valid.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        char = list(string.ascii_lowercase) + list(string.ascii_uppercase)
        self.dict = {}

        for i in range(0, len(char)):
            if (i < 26): # if lowercase
                self.dict[char[i]] = char[:26][(i + shift) % 26 ]
            else: # if uppercase
                self.dict[char[i]] = char[26:][(i + shift) % 26 ]

        return self.dict


    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        text = ""
        for e in self.get_message_text():
            if e in self.build_shift_dict(shift):
                e = self.dict[e]
            text += e
        return text



class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object

        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less
        code is repeated
        '''
        #print(self.message_text)
        Message.__init__(self, shift)
        self.message_text = text
        self.valid_words = self.valid_words
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)




    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class

        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class

        Returns: a COPY of self.encrypting_dict
        '''
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class

        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other
        attributes determined by shift (ie. self.encrypting_dict and
        message_text_encrypted).

        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object

        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        # print(self.message_text)
        # print(self.valid_words)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value and find the "best" one.

        We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift) on the message text.

        If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value for decrypting it.

        Note: if multiple shifts are  equally good such that they all create
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        You may find the helper function is_word(wordlist, word) and the string method split() useful. Note that is_word will ignore punctuation and other special characters when considering whether a word is valid.

        '''
        # inadequate solution that only covers a limited number of cases
        # no while loop, if you can't do for loop
        # while loop is prone to break

        # s = 0
        # list = self.apply_shift(s).split(" ")
        # while (s < 26 ): # from 0 to 25
        #     # make list of words then check
        #     list = self.apply_shift(s).split(" ")
        #     for word in list:
        #         if (not is_word(self.valid_words, word)):
        #             valid = False
        #             break
        #         else:
        #             print('valid')
        #             valid = True
        #     if (valid):
        #         break
        #     s += 1 # get out of for loop then increment
        # return (s, self.apply_shift(s))

        # variable to store a best shift
        # count valid words if it is higher then store


        current = (0, 0) # words, index
        for i in range (26): # iterate from 0 to 25
            textList = self.apply_shift(i).split(" ")
            nWords = len(list(filter(lambda word:is_word(self.valid_words, word), textList)))
            if (nWords > current[0]): # if this shift is more effective
                current = (nWords, i)
            if (nWords == len(textList)):
                break
        return(current[1], self.apply_shift(current[1]))

        #return(bestShift, self.apply_shift(bestShift))

        # arr = self.apply_shift(2).split(" ")
        # # string applying shift 2 into list
        # top = len(arr) # number of words in list
        # current = (0, 0) # words, index
        # for i in range(26): # from 0 to 25
        #     # make list of words then check
        #     arr = self.apply_shift(i).split(" ")
        #     found = len(list(filter(lambda word: is_word(self.valid_words, word), arr)))
        #     if (found > current[0]):
        #         current = (found, i)
        #     if (found == top):
        #         break
        # return (i, self.apply_shift(current[1]))




# test = Message('aBCde!!')
# print(test.apply_shift(2))
#Example test case (PlaintextMessage)
# plaintext = PlaintextMessage('abc', 2)
# print('Expected Output: cde')
# print('Actual Output:', plaintext.get_message_text_encrypted())
# plaintext.change_shift(1)
# print('Expected Output: bcd')
# print('Actual Output:', plaintext.get_message_text_encrypted())
#
# # #Example test case (CiphertextMessage)
# ciphertext = CiphertextMessage('Xyxcoxco gybnc: gszo byikvdi nsckzzokb mywzodsdyb cdkbd vswl cywogrobo zbywsco cdkxnkbn ohmovvoxmo byeqr cdoov drbyg vkxnvybn csd')
# print(ciphertext.message_text)
# print('Expected Output:', ('Nonsense words: wipe royalty disappear competitor start limb somewhere promise standard excellence rough steel throw landlord sit'))
# print('Actual Output:', ciphertext.decrypt_message())

def decrypt_story():
    '''
    graders will use our implementation of the Message, PlaintextMessage, and CiphertextMessage classes, so don't worry if you did not get the previous parts correct.

    Now that you have all the pieces to the puzzle, please use them to decode the file story.txt. The file ps6.py contains a helper function get_story_string() that returns the encrypted version of the story as a string. Create a CiphertextMessage object using the story string and use decrypt_message to return the appropriate shift value and unencrypted story string.

    '''
    encrytMessage = CiphertextMessage(get_story_string())
    # encrytMessage.message_text
    return encrytMessage.decrypt_message()

print(decrypt_story())
