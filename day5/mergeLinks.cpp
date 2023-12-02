#include <bits/stdc++.h>

using namespace std;

class SinglyLinkedListNode {
    public:
        int data;
        SinglyLinkedListNode *next;

        SinglyLinkedListNode(int node_data) {
            this->data = node_data;
            this->next = nullptr;
        }
};

class SinglyLinkedList {
    public:
        SinglyLinkedListNode *head;
        SinglyLinkedListNode *tail;

        SinglyLinkedList() {
            this->head = nullptr;
            this->tail = nullptr;
        }

        void insert_node(int node_data) {
            SinglyLinkedListNode* node = new SinglyLinkedListNode(node_data);
                    // cout << "inside insert node " << endl;

            if (!this->head) {
                this->head = node;
            } else {
                this->tail->next = node;
            }

            this->tail = node;
        }
};

void print_singly_linked_list(SinglyLinkedListNode* node, string sep, ofstream& fout) {
    while (node) {
        cout << node->data;

        node = node->next;

        if (node) {
            cout << sep;
        }
    }
}

void free_singly_linked_list(SinglyLinkedListNode* node) {
    while (node) {
        SinglyLinkedListNode* temp = node;
        node = node->next;

        free(temp);
    }
}

// Complete the mergeLists function below.

/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode* next;
 * };
 *
 */
SinglyLinkedListNode* mergeLists(SinglyLinkedListNode* head1, SinglyLinkedListNode* head2) {
    
    //check if some list are open
    if (head1 == nullptr && head2 == nullptr)
        return (nullptr);
    if (head1 == nullptr)
        return (head2);
    else if (head2 == nullptr)
        return (head1);
    

    //New sorted and merged linked list
    SinglyLinkedList *newList = new SinglyLinkedList();

    //Temporary pointers to hold the heads of the linked lists to not lose the original headq
    SinglyLinkedListNode *tmp1 = head1;
    SinglyLinkedListNode *tmp2 = head2;

    //traverse both linked list simultaneously and compare each element of each linked list 
    for(; tmp1 != nullptr && tmp2 != nullptr; ){
        if (tmp1->data < tmp2->data){
            newList->insert_node(tmp1->data);
            tmp1 = tmp1->next;
        }
        else{
            newList->insert_node(tmp2->data);
            tmp2 = tmp2->next;
        }
    }

    //copy the remaining elements of the linked lists 
    while(tmp1 != nullptr){
        newList->insert_node(tmp1->data);
        tmp1 = tmp1->next;
    }

    while(tmp2 != nullptr){
        newList->insert_node(tmp2->data);
        tmp2 = tmp2->next;
    }
    return (newList->head);
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int tests;
    cin >> tests;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int tests_itr = 0; tests_itr < tests; tests_itr++) {
        SinglyLinkedList* llist1 = new SinglyLinkedList();

        int llist1_count;
        cin >> llist1_count;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        for (int i = 0; i < llist1_count; i++) {
            int llist1_item;
            cin >> llist1_item;
            cin.ignore(numeric_limits<streamsize>::max(), '\n');

            llist1->insert_node(llist1_item);
        }
      
      	SinglyLinkedList* llist2 = new SinglyLinkedList();

        int llist2_count;
        cin >> llist2_count;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        for (int i = 0; i < llist2_count; i++) {
            int llist2_item;
            cin >> llist2_item;
            cin.ignore(numeric_limits<streamsize>::max(), '\n');

            llist2->insert_node(llist2_item);
        }

        SinglyLinkedListNode* llist3 = mergeLists(llist1->head, llist2->head);

        print_singly_linked_list(llist3, " ", fout);
        cout << "\n";

        free_singly_linked_list(llist3);
    }

    fout.close();

    return 0;
}
