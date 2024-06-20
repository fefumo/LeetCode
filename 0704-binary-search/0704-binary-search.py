class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        start = 0
        end = len(nums) - 1

        middle = (start + end) // 2

        if nums[middle] == target:
            return middle
        
        elif nums[middle] > target:
            return self.binary(nums, start, middle-1, target)

        elif nums[middle] < target:
            return self.binary(nums, middle+1, end, target)
    
    def binary(self, nums, start, end, target):
        middle = (start + end) // 2
        if start > end:
            return -1

        if nums[middle] == target:
            return middle
        
        elif nums[middle] > target:
            return self.binary(nums, start, middle-1, target)

        elif nums[middle] < target:
            return self.binary(nums, middle+1, end, target)
