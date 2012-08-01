from naive_guesser import NaiveGuesser

if __name__ == '__main__':

    for i in xrange(10):
        G = NaiveGuesser()
        word = G.new_word()

        stats = G.guess_word(word, verbose=False)
        for k,v in stats.iteritems():
            print "%s : %s" % (k.upper(), v)
        print ''

