def uniqueMorseRepresentations(words):
    MORSE = [".-","-...","-.-.","-..",".","..-.","--.",
     "....","..",".---","-.-",".-..","--","-.",
     "---",".--.","--.-",".-.","...","-","..-",
     "...-",".--","-..-","-.--","--.."]

    res = set()
    for word in words:
        word_morse = ''
        for c in word:
            word_morse += MORSE[ord(c) - ord('a')]
        res.add(word_morse)
    return len(res)
