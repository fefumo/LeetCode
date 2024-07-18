
class Solution {
public:
    int countPairs(TreeNode* root, int distance) {
        int answer = 0;
        dfs(root, distance, answer);
        return answer;
    }

    std::vector<int> dfs (TreeNode* root, int distance, int& answer){
        if (!root) return {};

        if (!root->left && !root->right){
            return {0};
        }

       std::vector<int> leftDist = dfs(root-> left, distance, answer);
       std::vector<int> rightDist = dfs (root->right, distance, answer);

        for (int l : leftDist){
            for (int r : rightDist){
                if (l + r + 2 <= distance){
                    answer ++;
                }
            }
        }

        std::vector<int> curDist;
        for(int l : leftDist){
            curDist.push_back(l + 1);
        }
        for (int r : rightDist){
            curDist.push_back(r + 1);
        }
       
       return curDist;
    }
};
