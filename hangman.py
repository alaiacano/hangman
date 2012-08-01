from naive_guesser import NaiveGuesser
import urllib2, re

if __name__ == '__main__':

    # Get the total number of guesses for every word 
    # in Jacob Bijani's list of obscenities.

    dirty_words = urllib2.urlopen('https://raw.github.com/jake/collections/master/profanities.txt').read()
    dirty_words = [i.strip() for i in dirty_words.split('\n')]

    total_guesses = 0
    for i, word in enumerate(dirty_words):
        G = NaiveGuesser()

        # keep only letters and apostrophe
        word = re.sub(r"[^a-z']", "", word)

        stats = G.guess_word(word, verbose=False)
        total_guesses += stats['guess_count']

        print "Word %s : %s Guesses (%s) : %s" % (i, word, stats['guess_count'], stats['guesses'])

    print "TOTAL WORDS:", len(dirty_words)
    print "TOTAL GUESSES:", total_guesses
