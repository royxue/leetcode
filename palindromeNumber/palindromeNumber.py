class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        orig = x
        reverse = 0
        if x >= 0:
            while x > 0:
                reverse = reverse*10 +  x%10
                x = x/10
            if orig == reverse:
                return True
            else:
                return False
        else:
            return False