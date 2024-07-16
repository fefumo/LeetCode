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
    bool isBalanced(TreeNode* root) {
        if (root == nullptr) return true;

        int left = leftDepth(root->left);
        int right = rightDepth(root->right);

        bool l = isBalanced (root->left);
        bool r = isBalanced(root->right);
        
        if (l == false || r == false) return false;
        if (abs(left - right) > 1) return false;
        return true;
    }
    int leftDepth(TreeNode* root){
        if (root == nullptr) return 0;

        int lh = leftDepth(root->left);
        int rh = rightDepth(root->right);

        if (lh > rh) return lh + 1;
        else return rh + 1;
    }
    int rightDepth(TreeNode* root){
        if (root == nullptr) return 0;

        int lh = leftDepth(root->left);
        int rh = rightDepth(root->right);

        if (lh > rh) return lh + 1;
        else return rh + 1;
    }
};