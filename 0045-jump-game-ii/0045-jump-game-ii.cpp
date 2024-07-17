class Solution {
public:
    int jump(std::vector<int>& nums) {
        int n = nums.size() - 1;
        if (nums.size() == 1) return 0;
        int curRange = 0;
        int farthest = 0;
        int count = 0;

        for (int i = 0; i < n; i ++){
            farthest = std::max(farthest, i + nums[i]);
            
            if (i == curRange){
                count += 1;
                curRange = farthest;

                if(curRange > n){
                    break;
                }
            }
        }

        return count;
    }
};