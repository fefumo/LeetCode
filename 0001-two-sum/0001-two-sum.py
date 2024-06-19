class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        for first_n in range(len(nums)):
            cur_first = nums[first_n]
            for second_n in range(1, len(nums)):
                cur_sec = nums[second_n]
                if cur_first + cur_sec  == target and second_n != first_n:
                    res.append(first_n)
                    res.append(second_n)
                    return res
        