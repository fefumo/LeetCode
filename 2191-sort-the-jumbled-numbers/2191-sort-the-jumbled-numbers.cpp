class Solution {
public:
    vector<int> sortJumbled(vector<int>& mapping, vector<int>& nums) {
        vector<pair<int,int>> mapped;

        for (auto num : nums){
            string strnum = to_string(num);
            int mapnum;
            for (int i = 0; i < strnum.size(); i++){
                int digit  = ((int) strnum[i]) - ((int)'0');
                int mapped_digit = mapping[digit];
                strnum[i] = static_cast<char>(mapped_digit + '0');
            }
            mapnum = stoi(strnum);
            mapped.push_back(make_pair(num, mapnum));
        }

        //for (auto i : mapped){
        //    cout << i.first << ", " << i.second << endl;
        //}
        //cout << endl;

        sort(mapped.begin(), mapped.end(),
            [](pair<int,int>& a, pair<int,int>& b){
                return a.second < b.second;
            }
        );
        
        //for (auto i : mapped){
        //    cout << i.first << ", " << i.second << endl;
        //}
        //cout << endl;

        vector<int> res;

        for(auto p : mapped){
            res.push_back(p.first);
        }

        
        return res;
    }
};