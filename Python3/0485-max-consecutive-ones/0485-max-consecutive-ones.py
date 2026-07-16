class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = maxConsec = 0

        for num in nums:
            if num:
                cnt += 1
                if cnt > maxConsec:
                    maxConsec = cnt
            else:
                cnt = 0
                
        return maxConsec