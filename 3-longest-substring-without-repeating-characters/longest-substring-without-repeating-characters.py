class Solution(object):
    def lengthOfLongestSubstring(self, s):
        p=''
        out=0
        
        for i in s:
            while i in p:
                p=p[1:]
            p+=i
            out=max(out,len(p))
            
        return out