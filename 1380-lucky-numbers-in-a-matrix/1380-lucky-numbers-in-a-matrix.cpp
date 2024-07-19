class Solution {
public:
    vector<int> luckyNumbers (vector<vector<int>>& matrix) {
        vector<int> res = {};
        vector<int> minRow = {};
        vector<int> maxCol = {};
        
        for (int i = 0; i < matrix[0].size(); i ++){
            int cur = matrix[0][i];
            int  colMax = cur;
            for (int j = 1; j < matrix.size(); j ++){
                colMax = max(colMax, matrix[j][i]);
            }
            maxCol.push_back(colMax);
        }
        for (auto arr : matrix){
            int rowMin = INT_MAX;
            for (auto elem : arr){
                rowMin = min(rowMin, elem);
            }
            minRow.push_back(rowMin);
        }
        
        for (int i = 0; i < minRow.size(); i++){
            for (int j = 0; j < maxCol.size(); j++){
                if (minRow[i] == maxCol[j]){
                    res.push_back(minRow[i]);
                }
            }
        }
        
        return res;
    }
};