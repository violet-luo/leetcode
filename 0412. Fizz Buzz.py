/*

Runtime: 36 ms, faster than 96.34% of Python3 online submissions for Fizz Buzz.
Memory Usage: 14.8 MB, less than 69.74% of Python3 online submissions for Fizz Buzz.

*/


def fizzBuzz(self, n: int):
    ans = []

    for i in range(1, n+1): #start with 1
        if i % 3 == 0 and i % 5 == 0:
            ans.append('FizzBuzz')
        elif i % 3 == 0:
            ans.append('Fizz')
        elif i % 5 == 0:
            ans.append('Buzz')
        else:
            ans.append(str(i)) #do not forget to convert int to str

    return ans
