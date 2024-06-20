class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            
            if nums[mid] >= nums[left]: #then mid is in the left sorted portion
                if target > nums[mid] or target < nums[left]: #then target is to the right of mid
                    left = mid + 1
                else:
                    #then target is to the left of mid
                    right = mid - 1                                    
            
            else: #then mid is in the right sorted portion
                if target < nums[mid] or target > nums[right]: #then target is to the left of mid 
                    right = mid - 1                                        
                else:
                    #then target is to the right of mid 
                    left = mid + 1
        
        return -1
