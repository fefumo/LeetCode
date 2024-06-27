class Solution {
public:
    int findCenter(vector<vector<int>>& edges) {
        for (int i{}; i < 2; ++i){
            if (edges[i][i] == edges[i+1][i] || edges[i][i] == edges[i+1][i+1]){
                return edges[i][i];
            }
            else if (edges[i][i+1] == edges[i+1][i] || edges[i][i+1] == edges[i+1][i+1]){
                return edges[i][i+1];
            }
        }
        return -1;
    }
};