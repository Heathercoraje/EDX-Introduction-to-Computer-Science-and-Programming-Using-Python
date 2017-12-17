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

    word_list (list): list of words in the dictionary.
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
        done = False
        s = 0
        while (not done):
            print(done)
            print('shift value: ', s)
            print('in progress')
            # make list of words then check
            list = self.apply_shift(s).split(" ") #
            print(list[:2]) # this must change each time
            for word in list:
                if (not is_word(self.valid_words, word)):
                # if give word is not valid word
                    s += 1
                    break
                    # self.message_text = self.apply_shift(s)
                else:# if all the word is valid word
                    done = True
                    return self.apply_shift(s)
        #return self.apply_shift(s)

# test = Message('aBCde!!')
# print(test.apply_shift(2))
#Example test case (PlaintextMessage)
# plaintext = PlaintextMessage('abc', 2)
# print('Expected Output: cde')
# print('Actual Output:', plaintext.get_message_text_encrypted())
# plaintext.change_shift(1)
# print('Expected Output: bcd')
# print('Actual Output:', plaintext.get_message_text_encrypted())

# #Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('dhkmjqz xjilpzno mzyyzi avxo rdaz zvmi yzovdg ocdif xgjocz kvnnvbz zqzmtjiz rjjgzi wzndyz xjno adibzm ngjr ajmzno mzxjhhziy npaazm jkzmvodji dhdovoz nzqzmz cjggjr voomvxodqz xjhkzoz vgocjpbc mpyz izxznnvmt piyzm ncjpgy wmdwzmt hpndx zaazxo gziboc yznompxodji')
print(ciphertext.message_text)
print('Expected Output:', (24, 'improve conquest redden fact wife earn detail think clothe passage everyone woolen beside cost finger slow forest recommend suffer operation imitate severe hollow attractive compete although rude necessary under should bribery music effect length destruction'))
print('Actual Output:', ciphertext.decrypt_message())
