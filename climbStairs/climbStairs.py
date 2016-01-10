class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2:
            return 1
        elif n==2:
            return 2
        l = [1, 1, 1]
        for i in range(2, n+1):
            l[i%3] = l[(i-1)%3]+l[(i-2)%3]
            print l
        return l[i%3]
        