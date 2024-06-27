class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        vector<int> res;
        for (int i{}; i < nums1.size(); ++i){
            int cur = nums1[i];
            int cnt = count(nums2.begin(), nums2.end(), cur);
            int cnt2 = count(res.begin(), res.end(), cur);
            if (cnt != 0 && cnt2 == 0){
                res.push_back(cur);
            }
        }
        return res;
    }
};