from guesser import Guesser
import re
import numpy as np

class NaiveGuesser(Guesser):
    '''
    get all words with this letter sequence
    get letter distribution of those letters
    return most likely letter
    '''
    def __init__(self):
        super(NaiveGuesser, self).__init__()
        self.__current_word = ''
        self.guessed_letters = []
        self.default_dist = self.get_letter_order('_')

    def guess_letter(self, incomplete_word):
        
        # get the letter order using the information in the incomplete word
        letter_order = self.get_letter_order(incomplete_word)

        # letter_order might not include ALL letters, so stick those on the end.
        letter_order.extend(self.default_dist)

        for letter in letter_order:
            if letter in self.guessed_letters:
                continue
            self.guessed_letters.append(letter)
            return letter

        # something's wrong.
        return -1


    def get_letter_order(self, incomplete_word):
        '''
        Wicked slow letter counting function.
        '''
        incomplete_word = re.sub('_+', '_', incomplete_word)
        pattern = re.sub('_', '.+', incomplete_word)
        self.available_words = [word for word in self.words if re.search(pattern, word)]
        
        letters = sorted(''.join(self.available_words))
        letters = np.array(letters)

        letter_count = {}
        for l in letters:
            try:
                letter_count[l] += 1
            except KeyError:
                letter_count[l] = 1

        letter_count = letter_count.items()
        order = np.argsort([l[1] for l in letter_count])
        order = order[::-1]
        retval = [letter_count[i][0] for i in order]
        if retval == []:
            retval = self.default_dist
        return retval