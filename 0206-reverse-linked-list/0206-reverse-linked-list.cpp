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
    ListNode* reverseList(ListNode* head) {
        ListNode* newLinkedList = nullptr;
        ListNode* current = head;
        ListNode* next_node = nullptr;
        while(current != nullptr){
            next_node = current->next;
            current->next = newLinkedList;
            newLinkedList = current;
            current = next_node;
        }
        return newLinkedList;
    }
};