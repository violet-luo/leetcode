def mahjong(tile):
    counter = collections.Counter(tile)
    pairs = 0

    for num, count in counter.items():
        remainder = count % 3
        if remainder == 1:
            return False
        if remainder == 2:
            pairs += 1

    return pairs == 1
