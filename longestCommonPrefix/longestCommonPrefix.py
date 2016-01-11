class Solution(object):
    def getPrefix(self, a, b):
        l = min(len(a), len(b))
        result = ''
        for i in range(l):
            if a[i] == b[i]:
                result += a[i]
            else:
                return result
        return result
            
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]
        result = self.getPrefix(strs[0], strs[1])
        for i in range(2, len(strs)):
            result = self.getPrefix(result, strs[i])
        return result
        