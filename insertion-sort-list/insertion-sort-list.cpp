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
    ListNode* insertionSortList(ListNode* head) {
    ListNode fake_head = ListNode(0, head);
    ListNode* cur = head->next;
    ListNode* prev = head;
    while (cur){

        if (cur -> val  >= prev ->val){
            prev = cur;
            cur = cur -> next;
        }

        else{
            prev -> next = cur -> next;
            ListNode* temp = &fake_head;

            while(cur -> val > temp -> next -> val){
                temp = temp->next;
            }
            cur -> next = temp -> next;
            temp -> next = cur;
            cur = prev -> next;
        }
    }
    
    return fake_head.next;
    }
};