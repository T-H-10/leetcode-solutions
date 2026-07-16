class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        duplicate = 0
        missing = 0
        
        for num in nums:
            x = abs(num)
            if nums[x - 1] < 0:
                duplicate = x
            else:
                nums[x - 1] *= -1

        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i+1
                break

        return [duplicate, missing]
