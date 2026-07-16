import math

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = n**2
        sumEven = sumOdd + n

        return math.gcd(sumOdd, sumEven)