class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows > len(s):
            return s
        iter = len(s)/numRows
        result = [[] for i in range(numRows)]
        idx = 0
        step = 0
        for i in range(len(s)):
            t = i%(numRows*2-2)
            if t>=numRows:
                t=2*numRows - t - 2
            result[t].append(s[i])
        res = ""
        for l in result:
            res += ''.join(l)
        return res