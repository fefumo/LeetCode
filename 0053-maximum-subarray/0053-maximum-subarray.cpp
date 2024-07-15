class Solution {
public:
    int maxSubArray(std::vector<int>& nums) {
        int maxSum = nums[0];
        int cur;
        int prev = nums[0];
        for (int i = 1; i < nums.size(); i++){
            cur = std::max(nums[i], prev + nums[i]);
            prev = cur; 
            maxSum = std::max(maxSum, cur); 
        }
        return maxSum;
    }
};