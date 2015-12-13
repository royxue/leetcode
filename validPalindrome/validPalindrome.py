class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join([x.lower() for x in s if x.isalpha() or x.isdigit()])
        for i in range(len(s)):
            if i < len(s)-1-i:
                if s[i] == s[len(s)-1-i]:
                    continue
                else:
                    return False
        return True