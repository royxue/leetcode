class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = ''.join([i for i in s if i.isalpha() or i.isspace()]).split()
        if len(s) == 0:
            return 0
        else:
            return len(s[-1])