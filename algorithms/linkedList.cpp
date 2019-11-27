#include <iostream>

using namespace std;

class Node
{
    public:
        int data;
        Node *next;
};

//printing the list
void print(Node *list)
{
    while(list->next != NULL)
    {
        cout << list->data << ", ";
        list = list->next;
    }
}
//insertion at the tail
void insertion(Node** head, int newX)
{
    //new Node
    Node *tail = new Node();
    //get the head reference
    Node *last = *head;
    tail->data = newX;
    tail->next = NULL;
    if (*head == NULL)  
    {  
        *head = tail;  
        return;  
    }  
    while(last->next != NULL)
    {
        last = last->next;
        last->next = tail;
    }
    
}
using namespace std;

int main()
{
    Node *head = NULL;
    head = new Node();
    Node *first = NULL;
    first = new Node();
    Node *second = NULL;
    second = new Node();
    
    head->data = 0;
    head->next = first;
    first->data = 1;
    first->next = second;
    second->data = 2;
    //second->next = NULL;
 
    //print(head);
    insertion(&head, 24);
    print(head);
   
    return 0;
}
