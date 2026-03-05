class Solution(object):
    def myAtoi(self, s):
        s = s.strip()           # remove leading and trailing spaces
        
        if len(s) == 0:
            return 0
        
        sign = 1
        i = 0
        
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1
        
        num = 0
        
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        
        num = sign * num
        
        # 32-bit range check
        if num < -2**31:
            return -2**31
        if num > 2**31 - 1:
            return 2**31 - 1
        
        return num