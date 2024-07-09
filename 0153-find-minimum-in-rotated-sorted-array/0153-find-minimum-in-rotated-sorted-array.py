class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        minn = 5999
        while left <= right:
            mid = (left + right) // 2
            minn = min(minn, nums[mid])
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] == nums[right]:
                 break
            elif nums[mid] < nums[left]:
                right = mid - 1
            else:
                left -= 1
        return minn
    