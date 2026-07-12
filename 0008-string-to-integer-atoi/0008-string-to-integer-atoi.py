class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        sign = 1
        res = 0
        
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # 1. Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1
        
        # 2. Handle sign
        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1
        
        # 3. Convert digits
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            
            # 4. Handle overflow
            if res > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            res = res * 10 + digit
            i += 1
        
        return sign * res
