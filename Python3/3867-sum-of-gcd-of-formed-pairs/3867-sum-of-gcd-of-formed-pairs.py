import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        maxNum = nums[0]
        prefixGcd = []
        for i in range(len(nums)):
            if nums[i] > maxNum:
                maxNum = nums[i]
            prefixGcd.append(math.gcd(nums[i], maxNum))
        print(prefixGcd)
        prefixGcd.sort()
        print(prefixGcd)
        i, j = 0, len(prefixGcd) - 1
        res = 0
        while i < j:
            res += math.gcd(prefixGcd[i], prefixGcd[j])
            i+=1
            j-=1

        return res
