class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0:
            return 0
        str = str.strip()
        count = ""
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        hint = ''
        if str[0] in ['-', '+']:
            hint = str[0]
            str = str[1:]
        for i in str:
            if i.isdigit():
                count += i
            else:
                break
        if len(count) == 0:
            return 0
        count = hint + count
        if int(count) > INT_MAX:
            return INT_MAX
        elif int(count) < INT_MIN:
            return INT_MIN
        else:
            return int(count)
            
        