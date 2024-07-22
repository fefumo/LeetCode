class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        vector <pair<int, string>> heightNamePairs;
        
        for (int i = 0; i < heights.size(); i++){
            heightNamePairs.emplace_back(heights[i], names[i]);
        }
        
        sort(heightNamePairs.begin(), heightNamePairs.end(), greater<pair<int, string>>());
        
        for (int i = 0; i < names.size(); i++){
            names[i] = heightNamePairs[i].second;
        }

        return names;
    }
};