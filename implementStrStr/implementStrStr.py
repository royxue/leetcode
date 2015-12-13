class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(needle)
        m = len(haystack)
        if n == 0:
            return 0
        if m < n:
            return -1
        for i in range(0, m - n+1):
            for j in range(0, n+1):
                if j == n:
                    return i
                if haystack[i+j] != needle[j]:
                    break
        return -1

print Solution().strStr("123", "123")