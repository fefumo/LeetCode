/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        std::vector<int> vec;
        while (head != nullptr){
            vec.push_back(head->val);
            head = head->next;
        }

        int leftIdx = left - 1;

        std::reverse(vec.begin() + leftIdx, vec.end() - (vec.size() - right));
        
        ListNode* newList = nullptr;
        ListNode* cur = new ListNode(vec[0]);
        newList = cur;

        for (int i = 1; i < vec.size(); i++){
            cur->next = new ListNode(vec[i]);
            cur = cur->next;
        }

        return newList;
    }
};
