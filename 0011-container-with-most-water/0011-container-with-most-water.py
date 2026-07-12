class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height) - 1
        max_con = 0
        while i < j:
            cur = min(height[i], height[j]) * (j - i)
            if max_con < cur:
                max_con = cur
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_con
