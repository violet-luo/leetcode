def countCharacters(self, words, chars):
    chars_counter = collections.Counter(chars)
    res = 0

    for word in words:
        word_counter = collections.Counter(word)
        if all([word_counter[c] <= chars_counter[c] for c in word_counter]):
            res += len(word)
    
    return res
