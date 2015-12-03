class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rn_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        temp = 0
        for i in s:
            if rn_dict[i] <= temp or temp == 0:
                result += rn_dict[i]
            else:
                result += rn_dict[i] - 2*temp
            temp = rn_dict[i]
        return result
        