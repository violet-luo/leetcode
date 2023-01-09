def areSentencesSimilar(self, sentence1, sentence2, similarPairs):
    if len(sentence1) != len(sentence2):
        return False
    
    dic = collections.defaultdict(set)
    for p in similarPairs:
        dic[p[0]].add(p[1])
        dic[p[1]].add(p[0])
    
    for i in range(len(sentence1)):
        w1, w2 = sentence1[i], sentence2[i]
        if w1 != w2 and w2 not in dic[w1]:
            return False
    return True

##

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
