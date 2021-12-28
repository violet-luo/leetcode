def nameDeduplication(self, names):
    unique_name = []
    dic = {}

    for name in names:
        name = name.lower()
        if name not in dic:
            unique_name.append(name)
            dic[name] = 1
    
    return unique_name

def nameDeduplication(self, names):
    unique_name = []
    visited = set()

    for name in names:
        name = name.lower()
        if name not in visited:
            unique_name.append(name)
            visited.add(name)
    
    return unique_name

