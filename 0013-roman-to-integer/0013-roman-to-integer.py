class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num=0
        prev=0
        for char in reversed(s):
            curr=dict[char]
            if(curr < prev):
                num-=curr
            else:
                num+=curr
            prev=curr
        return num