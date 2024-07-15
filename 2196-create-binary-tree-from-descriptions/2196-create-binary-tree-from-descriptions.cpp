/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* createBinaryTree(vector<vector<int>>& descriptions) {
        std::unordered_map<int, TreeNode*> hashmap;
        for (const auto& arr : descriptions){
            int parent_val = arr[0];
            int child_val = arr[1];
            int position = arr[2];

            if (hashmap.find(parent_val) == hashmap.end()){
                hashmap[parent_val] = new TreeNode(parent_val);
            }
            if (hashmap.find(child_val) == hashmap.end()){
                hashmap[child_val] = new TreeNode(child_val);
            }
            if (position == 0){
                hashmap[parent_val]->right = hashmap[child_val];
            }
            else{
                hashmap[parent_val]->left = hashmap[child_val];
            }

            
        }

        std::unordered_set<int> children;
        TreeNode* root = nullptr;    

        for (const auto& arr : descriptions){
            children.insert(arr[1]);    
        }
        for (const auto& arr : descriptions){
            if (children.find(arr[0]) == children.end()){
                root = hashmap.at(arr[0]);
                break;
            }
        }
        return root;
    }
};