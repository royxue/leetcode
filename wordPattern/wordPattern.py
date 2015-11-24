class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        a_ = list(pattern)
        b_ = str.split(' ')
        return True if len(set(a_)) == len(set(b_)) and len(set(a_)) == len(set(zip(a_, b_))) and len(a_) == len(b_) else False