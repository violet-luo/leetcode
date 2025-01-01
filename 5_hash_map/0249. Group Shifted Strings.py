# {
#      (1, 1): ['abc', 'bcd', 'xyz'],  
#   (2, 2, 1): ['acef'],   
#       (25,): ['az', 'ba'],   
#          (): ['a', 'z']
# }

def groupStrings(self, strings: List[str]) -> List[List[str]]:
    shift_to_strings = collections.defaultdict(list)

    for s in strings:
        shift = ()
        for i in range(1, len(s)):
            diff = (ord(s[i]) - ord(s[i - 1])) % 26
            # Tuples are immutable, so cannot modify directly (e.g., by appending elements)
            # Instead, can create a new tuple by concatenating an existing tuple with another tuple
            # (diff,) creates a single-element tuple containing diff
            # e.g. diff = 1, x = (diff,) = (1, )
            shift += (diff, )
        shift_to_strings[shift].append(s)
    
    return list(shift_to_strings.values())
