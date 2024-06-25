class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;
        if (nums.size() == 1){
            return nums[0];
        }
        while (left <= right){
            int mid = left + (right - left) / 2;

            if (mid < nums.size() - 1 && nums[mid] > nums[mid + 1]){
                return nums[mid + 1];
            }
            else if (mid > 0 && nums[mid] < nums[mid - 1]){
                return nums[mid];
            }
            else if (nums[nums.size() - 1] > nums[mid]){
                right = mid - 1;
            }
            else{
                left = mid + 1;
            }
        }
        return nums[left];
    }
};