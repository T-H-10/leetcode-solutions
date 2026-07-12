class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ms = 1
        mi = 0
        
        for i in range(len(s)):
            
            up, down = i+1, i-1
            while up < len(s) and down >=0 and s[up] == s[down]:
                up += 1
                down -= 1
            else:
                cur_len = up - down - 1
                if cur_len > ms:
                    ms = cur_len
                    mi = down + 1
              
            up, down = i+1, i
            while up < len(s) and down >=0 and s[up] == s[down]:
                up += 1
                down -= 1
            else:
                cur_len = up - down - 1
                if cur_len > ms:
                    ms = cur_len
                    mi = down + 1   
                       
        return s[mi:mi + ms]
                
                
                
                
                
                 