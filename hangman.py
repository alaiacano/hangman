from naive_guesser import NaiveGuesser
import urllib2, re

if __name__ == '__main__':

    # Get the total number of guesses for every word 
    # in Jacob Bijani's list of obscenities.

    dirty_words = urllib2.urlopen('https://raw.github.com/jake/collections/master/profanities.txt').read()
    dirty_words = [i.strip() for i in dirty_words.split('\n')]

    total_guesses = 0
    wins = 0
    losses = 0
    for word in dirty_words:
        G = NaiveGuesser()

        # keep only letters and apostrophe
        word = re.sub(r"[^a-z']", "", word)

        stats = G.guess_word(word, verbose=False)
        total_guesses += stats['guess_count']
        if stats['success']:
            success = 'WIN '
            wins += 1
        else:
            success = 'LOSE'
            losses += 1
        print "%s Word: %s Guesses (%s): %s" % (success, word, stats['guess_count'], stats['guesses'])

    print "TOTAL WORDS:", len(dirty_words)
    print "TOTAL GUESSES:", total_guesses
    print "TOTAL WINS:", wins
    print "TOTAL LOSSES:", losses
    print "WIN PERCENT:", 100.*(wins*1./(wins+losses))