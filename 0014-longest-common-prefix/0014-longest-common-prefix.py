class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res=""
        i=0
        lens= [len(s) for s in strs]
        l=min(lens)
        while i<l:
            for s in strs[1:]:
                if(strs[0][i]!=s[i]):
                    return res
            res+=strs[0][i]
            i+=1
        return res