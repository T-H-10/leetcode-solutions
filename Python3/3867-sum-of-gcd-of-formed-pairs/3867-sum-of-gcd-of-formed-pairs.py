import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        maxNum = nums[0]
        prefixGcd = []

        for num in nums:
            if num > maxNum:
                maxNum = num

            prefixGcd.append(math.gcd(num, maxNum))

        prefixGcd.sort()
        i, j = 0, len(prefixGcd) - 1
        res = 0
        
        while i < j:
            res += math.gcd(prefixGcd[i], prefixGcd[j])
            i+=1
            j-=1

        return res
