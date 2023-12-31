# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    secret_word_length=len(secret_word)
    secret_letters_guessed = 0 
    
    for secret_letter in secret_word:
        if(secret_letter in letters_guessed):
            secret_letters_guessed += 1
    if(secret_letters_guessed ==secret_word_length):
        return True
    else:
        return False
                    
                
    pass   
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
# print(is_word_guessed('apples', ['e', 'a', 'k', 'p', 'l', 's']))
      
      
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    partially_guessed_word = ''
    
    for secret_letter in secret_word:
        
        if(secret_letter in letters_guessed):
            partially_guessed_word = partially_guessed_word + secret_letter
        else:
            partially_guessed_word = partially_guessed_word + '_ '
        
    return partially_guessed_word
                
    pass            
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
# secret_word = 'apple'  
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's'] 
# print(get_guessed_word(secret_word, letters_guessed)) 


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters =string.ascii_lowercase
    for letter_guessed in letters_guessed:
        if letter_guessed in available_letters:
            available_letters = available_letters.replace(letter_guessed,'')
            
    return available_letters    
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass
# letters_guessed = ['A','b','b','c'] 
# print(get_available_letters(letters_guessed))    
  

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    secret_word_length = len(secret_word)
    remaining_guesses = 6
    remaining_warnings = 3
    letters_guessed =['']
    availabe_letters = get_available_letters(letters_guessed)
    guessed_word =get_guessed_word(secret_word, letters_guessed)
    
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is',secret_word_length,'letters long.')
    print('You have',remaining_warnings,'warnings left.')
    
    
    
    while(remaining_guesses>0):
        
        
        print('_ ' * 10)
        print('You have',remaining_guesses,'guesses left.')
        print('Available letters:',availabe_letters)
        letter_guessed=input('Please guess a letter:')
        
        
        is_letter_alphabetic =str.isalpha(letter_guessed)
        
        if(letter_guessed not in availabe_letters):
            if(is_letter_alphabetic):
                warning_message = 'Oops! You \'ve already guessed that letter.'
            else:
                warning_message = 'Oops! That is not a valid letter.'
            if(remaining_warnings>0):
                remaining_warnings -=1
                print(warning_message,'You have',remaining_warnings,'warnings left:')
                print(guessed_word)
            else:
                remaining_guesses -=1
                print(warning_message,'You have no warning left')
                print('so you lose one guess:',guessed_word)

            continue    
        else:
            lower_case_letter_guessed = str.lower(letter_guessed)
        
        
        letters_guessed.append(lower_case_letter_guessed)
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        availabe_letters = get_available_letters(letters_guessed)
        is_word_correct_guessed = is_word_guessed(secret_word, letters_guessed) 
        
        if(is_word_correct_guessed):
            unique_secret_letters = len(set(secret_word))
            total_score = remaining_guesses *unique_secret_letters
            print('Good guess:',guessed_word)
            print('_ ' * 10)
            print('Congratulations, you won!')
            print('Your total score for this game is:',total_score)
            break
        elif(lower_case_letter_guessed in secret_word):
            print('Good guess:',guessed_word)    
        else:
            if(lower_case_letter_guessed in 'aeiou' and remaining_guesses>1):
                remaining_guesses -= 2
            else:
                remaining_guesses -= 1
            print('Oops! That letter is not in my word:',guessed_word)
            
        
    if(remaining_guesses == 0):
        print('_ ' * 10)
        print('Sorry, you ran out of guesses. The word was',secret_word)
        
                     
               
               
        
        
         
         
           
       
            
        
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word_without_spaces = my_word.replace(' ','')
    
    number_of_matching_letters =0
    if(len(my_word_without_spaces) == len(other_word)):
        for i in range(len(other_word)):
            
            if (my_word_without_spaces[i] == other_word[i]):
                number_of_matching_letters +=1
            elif (my_word_without_spaces[i] != '_'):
                return False
            elif(other_word[i] not in my_word_without_spaces):
                number_of_matching_letters +=1
    
        if(number_of_matching_letters ==len(other_word)):
            return True
        else:
            return False
    else:
        return False
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass
# print(match_with_gaps("a_ _ le", "banana"))
def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_matches =[]
    for secret_word in wordlist:
        if(match_with_gaps(my_word, secret_word)):
            possible_matches.append(secret_word)
    if(possible_matches == []):
        print('No matches found')
    else:
        print('Possible word matches are:')
        for possible_match in possible_matches:
            print(possible_match)
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass

# show_possible_matches("a_ pl_ ")


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    secret_word_length = len(secret_word)
    remaining_guesses = 6
    remaining_warnings = 3
    letters_guessed =['']
    availabe_letters = get_available_letters(letters_guessed)
    guessed_word =get_guessed_word(secret_word, letters_guessed)
    
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is',secret_word_length,'letters long.')
    print('You have',remaining_warnings,'warnings left.')
    
    
    
    while(remaining_guesses>0):
        
        
        print('_ ' * 10)
        print('You have',remaining_guesses,'guesses left.')
        print('Available letters:',availabe_letters)
        letter_guessed=input('Please guess a letter:')
        
        if(letter_guessed == '*'):
            show_possible_matches(guessed_word)
            continue
        
        is_letter_alphabetic =str.isalpha(letter_guessed)
        
        if(letter_guessed not in availabe_letters):
            if(is_letter_alphabetic):
                warning_message = 'Oops! You \'ve already guessed that letter.'
            else:
                warning_message = 'Oops! That is not a valid letter.'
            if(remaining_warnings>0):
                remaining_warnings -=1
                print(warning_message,'You have',remaining_warnings,'warnings left:')
                print(guessed_word)
            else:
                remaining_guesses -=1
                print(warning_message,'You have no warning left')
                print('so you lose one guess:',guessed_word)

            continue    
        else:
            lower_case_letter_guessed = str.lower(letter_guessed)
        
        
        letters_guessed.append(lower_case_letter_guessed)
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        availabe_letters = get_available_letters(letters_guessed)
        is_word_correct_guessed = is_word_guessed(secret_word, letters_guessed) 
        
        if(is_word_correct_guessed):
            unique_secret_letters = len(set(secret_word))
            total_score = remaining_guesses *unique_secret_letters
            print('Good guess:',guessed_word)
            print('_ ' * 10)
            print('Congratulations, you won!')
            print('Your total score for this game is:',total_score)
            break
        elif(lower_case_letter_guessed in secret_word):
            print('Good guess:',guessed_word)    
        else:
            if(lower_case_letter_guessed in 'aeiou' and remaining_guesses>1):
                remaining_guesses -= 2
            else:
                remaining_guesses -= 1
            print('Oops! That letter is not in my word:',guessed_word)
            
        
    if(remaining_guesses == 0):
        print('_ ' * 10)
        print('Sorry, you ran out of guesses. The word was',secret_word)
        
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
