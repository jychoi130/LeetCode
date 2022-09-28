import math

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        for i in range(0, int(math.ceil(float(len(s)//2)))):
            str(s[i])
            str(s[len(s)-i-1])
            if(s[i] != s[len(s)-i-1]):
                tmp = s[i]
                s[i] = s[len(s)-i-1]
                s[len(s)-i-1] = tmp
        
                
            