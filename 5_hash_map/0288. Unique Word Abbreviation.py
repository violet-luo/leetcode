class ValidWordAbbr:
    def __init__(self, dictionary):
        self.map = {}
        for word in dictionary:
            abbr = self.word_to_abbr(word)
            if abbr not in self.map:
                self.map[abbr] = set() 
            self.map[abbr].add(word)

    def word_to_abbr(self, word):
        if len(word) <= 1:
            return word
        return word[0] + str(len(word[1:-1])) + word[-1]
        
    def isUnique(self, word):
        abbr = self.word_to_abbr(word)
        if abbr not in self.map:
            return True
        for word_in_dict in self.map[abbr]:
            if word != word_in_dict:
                return False
        return True
