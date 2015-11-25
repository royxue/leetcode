class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx = [x for x in range(len(nums))]
        d = dict(zip(nums, idx))
        for i in range(len(nums)):
            if d.get(target - nums[i]):
                return [i+1, d.get(target-nums[i])+1]
        return "No such pair"
