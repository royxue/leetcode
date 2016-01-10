class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        init = "1"
        for i in range(n-1):
            num = 0
            pre = ""
            nextInit = ""
            for i in init:
                if pre!="" and pre!=i:
                    nextInit += str(num) + pre
                    num = 1
                else:
                    num += 1
                pre = i
            nextInit += str(num) + pre
            init = nextInit
        return init
