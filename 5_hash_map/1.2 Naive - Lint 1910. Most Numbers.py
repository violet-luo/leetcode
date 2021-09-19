def findNumber(self, array: List[int]) -> int:
    counter = collections.Counter(array)
    answer = 0
    max_number = 0

    for key, value in counter.items():
        if value > max_number:
            max_number = value
            answer = key
        elif value == max_number and key < answer:
            answer = key

    return answer
