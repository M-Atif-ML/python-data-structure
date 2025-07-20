#include<iostream>
using namespace std;
class Node{
    public:
    int data;
    Node* next;
    Node(int data,Node* next = nullptr):data(data),next(next){}
    int getData() const{
        return data;
    }
};
int main(){
    Node* head = new Node(1);
    Node* second = new Node(2);
    Node* third = new Node(3);
    Node* fourth = new Node(4);

    head->next = second;
    second->next = third;
    third -> next = fourth;
    fourth->next = nullptr;
    

    Node *current = head;
    while (current != nullptr){
        cout<<current->getData()<<"--->";
        if (current->data == 2) {
            current->next = current->next->next; // remove the node with data 3
            // break;
        }
        current = current->next;
    }
    cout<<endl;
    return 0;
}