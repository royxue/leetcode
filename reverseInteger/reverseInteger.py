class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reverse = 0
        if x < 0:
            a = -1
            x *= a
        else:
            a = 1
        while x > 0:
            reverse = reverse*10 + x%10
            x = x/10
        if reverse > 2147483647 or reverse < -2147483648:
            return 0
        return a*reverse
        
        