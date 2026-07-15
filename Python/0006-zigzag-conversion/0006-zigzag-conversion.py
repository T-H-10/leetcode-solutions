class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        if numRows == 1 or numRows >= len(s):
            return s
        
        res = [""] * numRows
        cur = 0
        direction = -1
        
        for c in s:
            res[cur] += c
            if cur == 0 or cur == numRows - 1:
                direction *= -1
            cur += direction
            
        return "".join(res)