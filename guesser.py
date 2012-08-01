import random, time
import numpy as np

WORDS = set([i.strip() for i in open('words.txt', 'r').readlines()])

class Guesser(object):
    '''
    Base object for word guesser.
    '''
    def __init__(self):
        """
        Super class init function. Put the following in the
        subclass's __init__ function:

        super(NaiveGuesser, self).__init__()
        """
        self.words = [i.lower() for i in WORDS if not '<' in i]

    def new_word(self):
        '''
        Return a random word from the list.
        '''
        return random.sample(self.words, 1)[0]

    def guess_letter(self, incomplete_word):
        """
        Here's what you need to make.

        Input:
        incomplete_word : A word with the letters that have been guessed 
                          so far filled in. The un-guessed words will be
                          underscores. Example: "e_am_le"

        Output:
        A single letter.
        """
        pass

    def guess_word(self, word, verbose=False):
        
        incomplete_word = ['_']*len(word)
        guesses = []
        correct_letters = 0
        word = list(word)
        tic = time.time()
        while correct_letters < len(word):
            guess = self.guess_letter(''.join(incomplete_word))
            if verbose == True:
                print guess
            guesses.append(guess)

            for i, l in enumerate(word):
                if l==guess:
                    correct_letters += 1
                    incomplete_word[i] = guess
                    if verbose == True:
                        print ''.join(incomplete_word)
        toc = time.time()
        
        guess_stats = {
            'word'           : ''.join(word),
            'unique_letters' : len(set(word)),
            'guess_count'    : len(guesses),
            'guesses'        : guesses,
            'time'           : round(1000*(toc-tic), 1),
            'success'        : len(guesses) - len(set(word)) < 9
        }
        return guess_stats
