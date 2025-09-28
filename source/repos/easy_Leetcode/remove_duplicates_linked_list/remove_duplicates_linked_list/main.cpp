
#include <iostream>
#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (!head)
        {
            return nullptr;
        }
        ListNode* current = head->next;
        ListNode* previous = head;
        while (current != nullptr)
        {
            if (current->val == previous->val)
            {
                previous->next = current->next;
                delete current;
                current = previous->next;
            }
            else
            {
                previous = current;
                current = current->next;
            }
        }
        return head;
    }
};

// Helper to build list from array
ListNode* buildList(const vector<int>& vals) {
    if (vals.empty()) return nullptr;
    ListNode* head = new ListNode(vals[0]);
    ListNode* current = head;
    for (size_t i = 1; i < vals.size(); i++) {
        current->next = new ListNode(vals[i]);
        current = current->next;
    }
    return head;
}

// Helper to print list
void printList(ListNode* head) {
    while (head) {
        cout << head->val;
        if (head->next) cout << " -> ";
        head = head->next;
    }
    cout << endl;
}

// Helper to free memory
void freeList(ListNode* head) {
    while (head) {
        ListNode* temp = head;
        head = head->next;
        delete temp;
    }
}

// Main test cases
int main() {
    Solution sol;

    // Test 1: Normal case with duplicates
    vector<int> vals1 = { 1, 1, 2, 3, 3 };
    ListNode* list1 = buildList(vals1);
    cout << "Original: ";
    printList(list1);
    list1 = sol.deleteDuplicates(list1);
    cout << "Cleaned:  ";
    printList(list1);
    freeList(list1);

    // Test 2: All elements are duplicates
    vector<int> vals2 = { 2, 2, 2, 2 };
    ListNode* list2 = buildList(vals2);
    cout << "\nOriginal: ";
    printList(list2);
    list2 = sol.deleteDuplicates(list2);
    cout << "Cleaned:  ";
    printList(list2);
    freeList(list2);

    // Test 3: No duplicates
    vector<int> vals3 = { 1, 2, 3, 4 };
    ListNode* list3 = buildList(vals3);
    cout << "\nOriginal: ";
    printList(list3);
    list3 = sol.deleteDuplicates(list3);
    cout << "Cleaned:  ";
    printList(list3);
    freeList(list3);

    // Test 4: Single element
    vector<int> vals4 = { 7 };
    ListNode* list4 = buildList(vals4);
    cout << "\nOriginal: ";
    printList(list4);
    list4 = sol.deleteDuplicates(list4);
    cout << "Cleaned:  ";
    printList(list4);
    freeList(list4);

    // Test 5: Empty list
    vector<int> vals5 = {};
    ListNode* list5 = buildList(vals5);
    cout << "\nOriginal: ";
    printList(list5);
    list5 = sol.deleteDuplicates(list5);
    cout << "Cleaned:  ";
    printList(list5);
    freeList(list5);

    return 0;
}