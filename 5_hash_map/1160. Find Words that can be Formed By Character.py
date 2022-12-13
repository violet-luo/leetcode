import collections
def countCharacters(words, property):
    property_cnt = collections.Counter(property)
    ans = 0
    for word in words:
        word_cnt = collections.Counter(word)
        for c in word_cnt:
            if property_cnt[c] < word_cnt[c]:
                break
            else:
                return word
    return '-'
