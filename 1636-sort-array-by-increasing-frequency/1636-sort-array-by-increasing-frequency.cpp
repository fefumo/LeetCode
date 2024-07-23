class Solution {
public:
    vector<int> frequencySort(vector<int>& nums) {
        map<int, int> hm;
        for (auto num : nums){
            if (hm.find(num) == hm.end()){
                hm[num] = 1;
            }
            else{
                hm[num] += 1;
            }
        }
        vector<pair<int,int>> vec (hm.begin(), hm.end());

        sort(vec.begin(), vec.end(), Solution::freqComparison);
        vector<int> res;
        for (auto i : vec){
            for(int j = 0; j < i.second; j++){
            res.push_back(i.first);
            }
        }
        return res;
    }

private:
    static bool freqComparison(const pair<int,int>& a, const pair<int,int>& b){
        if (a.second == b.second)
            return a.first > b.first;
        else
            return a.second < b.second;
    }
};