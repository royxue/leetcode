class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return round(3**round(math.log(n, 3))) == n if n>0 else False