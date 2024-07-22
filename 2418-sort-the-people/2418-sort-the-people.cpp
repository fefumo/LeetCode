class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        int i = 0;
        bool swapped;
        int n = heights.size();
        do{
            swapped = false;
            for (int i = 0; i < n - 1; i++){
                if (heights[i] < heights[i+1]){
                    iter_swap(heights.begin() + i, heights.begin() + (i + 1));
                    iter_swap(names.begin() + i, names.begin() + (i + 1));
                    swapped = true;
                }
            }
            --n;
        }while (swapped);

        return names;
    }
};