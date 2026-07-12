class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        i=1
        while i<len(nums):
            if nums[i]!=nums[k]:
               nums[k+1]=nums[i]
               k+=1
            i+=1
        print(nums)
        return k+1   
            


