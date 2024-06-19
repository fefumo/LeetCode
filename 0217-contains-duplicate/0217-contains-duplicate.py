class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        hs = set()
        for num in nums:
            if hs.__contains__(num):
                return True
            hs.add(num)
        
        return False