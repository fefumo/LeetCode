class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curNum = nums[0]
        dups = 0
        first = -1 # first duplicate in a sequence
        count = 0
        for i in range(1, len(nums)):
            #duplicate
            if curNum == nums[i]:
                dups += 1
                count += 1
                if (first == -1): # initiating 
                    first = i
            #new number
            else:
                if (dups != 0):
                    nums[first] = nums[i]
                    dups = 0
                    first += 1
                    
                else:
                    if nums[i] > nums[i-1] and first != -1:
                        nums[first] = nums[i]
                        first += 1
                    # else:
                        # dups += 1
                
                curNum = nums[i]
        
        # print(nums, end=" ")
        return len(nums) - count
