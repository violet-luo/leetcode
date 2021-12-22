def areSentencesSimilar(sentence1, sentence2, similarPairs):
    if len(sentence1) != len(sentence2):
        return False

    sets = set()
    for a, b in similarPairs:
        sets.add((a,b)) #(('great', 'fine'))
    
    for w, v in zip(sentence1, sentence2):
        if w != v and (w,v) not in sets and (v,w) not in sets:
            return False
    return True
