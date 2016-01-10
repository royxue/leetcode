class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        hist = set([])
        while n!=1 and n not in hist:
            hist.add(n)
            sum = 0
            while n:
                num = n%10
                sum += num*num
                n = n/10
            n = sum
        return n==1