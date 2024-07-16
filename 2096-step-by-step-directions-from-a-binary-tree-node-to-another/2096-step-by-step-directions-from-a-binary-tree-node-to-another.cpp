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
    std::string getDirections(TreeNode* root, int startValue, int destValue) {
        TreeNode* LCA = findLCA(root, startValue, destValue);
        std::string path = "";
        std::string path2 = "";
        int numberOfNodesToStartValue = 0;
        int numberOfNOdesToEndValue = 0;

        findPath(LCA,startValue, path, numberOfNodesToStartValue);
        findPath(LCA, destValue, path2, numberOfNOdesToEndValue);

        reverse(path2.begin(), path2.end());
        path = std::string(numberOfNodesToStartValue, 'U');
        //path2 = swapDirections(path2);
        path.append(path2);
        return path;
    }

    TreeNode* findLCA(TreeNode* root, const int& left, const int& right){
        if (root == nullptr || root->val == left || root->val == right) return root;

        TreeNode* lRoot = findLCA(root->left, left, right);
        TreeNode* rRoot = findLCA(root->right, left, right); 

        if (lRoot == nullptr){
            return rRoot;
        }
        else if (rRoot == nullptr){
            return lRoot;
        }
        else{ // both are not null, found node
            return root;
        }
    }

    bool findPath(TreeNode* root, int key, std::string& str, int& num){
        if (!root) return false;

        if(root->val == key) return true; 

        if (root -> left && findPath(root->left, key, str, num)){
                num += 1;
                str.push_back('L');
                return true;
            }
        if (root-> right && findPath(root->right, key, str, num)){
            num += 1;
            str.push_back('R');
            return true;
        }
        
        //str.pop_back();
        //num--;

        return false; 
    }

    //std::string swapDirections(const std::string& path) {
    //    std::string swappedPath = path;
    //    for (char& ch : swappedPath) {
    //        if (ch == 'L') {
    //            ch = 'R';
    //        } else if (ch == 'R') {
    //            ch = 'L';
    //        }
    //    }
    //    return swappedPath;
    //}
};