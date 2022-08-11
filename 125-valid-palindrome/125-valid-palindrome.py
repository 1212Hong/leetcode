class Solution(object):
    def isPalindrome(self, s):
        result = []
        for i in s:
            if i.isalnum():
                result.append(i.lower())
        
        while len(result)>1:
            if result.pop(0) != result.pop():
                return False
            
        return True
        """
        :type s: str
        :rtype: bool
        """
        