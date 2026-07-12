class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = defaultdict(lambda: -1)
        idx = 0
        ms = 0
        for i, c in enumerate(s):
            if  d[c] >= idx:
                ms = max (ms , i - idx)
                idx = d[c] + 1
            d[c] = i    
        return max(ms, len(s)- idx)    