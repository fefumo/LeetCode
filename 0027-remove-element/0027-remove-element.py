class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        cnt = 0
        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                cnt += 1
            else:
                nums[k] = nums[i]
                k += 1
        return len(nums) - cnt