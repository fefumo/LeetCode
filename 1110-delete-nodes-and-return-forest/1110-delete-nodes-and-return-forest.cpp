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
    std::vector<TreeNode*> delNodes(TreeNode* root, std::vector<int>& to_delete) {
                
        std::vector<TreeNode*> survivedNodes;
        if (std::find(to_delete.begin(), to_delete.end(), root->val) == to_delete.end()){
            survivedNodes.push_back(root);
        }
        deleteNodes(root, to_delete, survivedNodes);
        return survivedNodes;
    }

    TreeNode* deleteNodes(TreeNode* root, std::vector<int>& to_delete, std::vector<TreeNode*>& nodes){ 
        if (root == nullptr) return nullptr;
        
        root -> left = deleteNodes(root->left, to_delete, nodes);
        root -> right = deleteNodes(root->right, to_delete, nodes);

        if (std::find(to_delete.begin(), to_delete.end(), root->val) != to_delete.end()){
            if (root -> left){
                nodes.push_back(root -> left);
            }
            if (root -> right){
                nodes.push_back(root -> right);
            }
            return nullptr;
        }

        return root;
    }
};