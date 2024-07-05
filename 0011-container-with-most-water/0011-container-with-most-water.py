class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        left_idx = 0
        right_idx = len(height)-1
        for i in range(len(height)):
            left_pointer = height[left_idx]
            right_pointer = height[right_idx]
            #calc area
            curr_height = min(left_pointer, right_pointer)
            idx_diff = right_idx - left_idx
            cur_area = curr_height * idx_diff
            area = max(area, cur_area)
            if left_pointer < right_pointer:
                left_idx += 1
            else:
                right_idx -= 1
        
        return area 