class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int left = 0, right = nums.size() - 1;
        int edge_case = nums.size() - 1;
        int edge_case2 = 0;
        if (nums.size() == 1){
            return 0;
        }
        
        while (left <= right){
            int mid = left + (right - left) / 2;

            if ( (mid == edge_case && nums[mid] > nums[mid - 1]) ||
            (mid == edge_case2 && nums[mid] > nums [mid + 1]) ){
                return mid;
            }
            else if (nums[mid] > nums[mid + 1] && nums[mid] > nums[mid - 1]){
                return mid;
            }
            else if (nums[mid + 1] > nums[mid]){
                left = mid + 1;
            }
            else{
                right = mid - 1;
            }
        }
        return 0;
    }
};