# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        head = 1
        tail = n
        while head<=tail:
            mid = (head + tail)/2
            if isBadVersion(mid):
                tail = mid -1
            else:
                head = mid + 1
        return head
        