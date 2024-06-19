class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cur_value = 0
        for i in range(1, len(nums)):
            cur_value = nums[i-1]
            nums[i] += cur_value
        return nums