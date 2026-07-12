class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        dict={'(':')','{':'}','[':']'}
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            elif len(stack)==0 or ch!=dict[stack.pop()]:
                    return False
        return len(stack)==0