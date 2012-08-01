# Hangman game.

This is a fun game to see how well a program can play hangman. There's a list of 20,137 words that I got from https://github.com/trinker/hangman.

There's a base `Guesser` class that you can extend with your own `guess_letter` method. It provides the following to you:

* `words` - a list of all words in the data set, all in lower case. It's fair to use this list to calculate letter probabilities.
* `new_word()` - just returns a random word from the list
* `guess_word(word)` - executes the `guess_letter` method repeatedly until the word is guessed.

The `guess_letter` method takes a string as an input which has the current status of the game. 

To explain by example, if the word is "randomness", the first input to `guess_letter` would be `__________`. If an 'e' is guessed, the second input to `guess_letter` would be `_______e__`.

# NaiveGuesser

My letter guesser takes the following strategy:

* Find all possible words that will fit in the current pattern. If the current guess is `r__d__n_ss`, it uses words that match the regex `r.+d.+n.+ss`
* Of those words, calculate the letter distribution.
* Return the most likely letter that hasn't already been guessed

# Example

Here's an example of how to execute the `NaiveGuesser`:

```python
G = NaiveGuesser()
word = G.new_word()

stats = G.guess_word(word, verbose=False)
print stats
```

The output is:

```javascript
{
    "guesses": ["e", "r", "t", "a", "i", "n", "o", "s", "c", "u", "m", "h", "g"], 
    "unique_letters": 8, 
    "success": true, 
    "guess_count": 13, 
    "time": 770.8, 
    "word": "chemurgic"
}
```

## Testing on dirty words.

I tested the hangman guesser against a [list of dirty words](https://github.com/jake/collections/blob/master/profanities.txt). It did not perform very well:

    TOTAL WORDS: 505
    TOTAL GUESSES: 9236
    TOTAL WINS: 94
    TOTAL LOSSES: 411
    WIN PERCENT: 18.6138613861