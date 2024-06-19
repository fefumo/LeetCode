class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        a = m - 1
        b = n - 1
        c = m + n - 1
        
        while b >= 0:
            if a >= 0 and nums1[a] >= nums2[b]:
                nums1[c] = nums1[a]
                a -= 1
                c -= 1
            else:
                nums1[c] = nums2[b]
                b -= 1
                c -= 1
