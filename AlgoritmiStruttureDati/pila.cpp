#include <iostream>
using namespace std;

struct node{
    node* prevNode;
    int value;

};
class Pila{
    private:
        node *head, *linkedList;
        int size;
    public:
        Pila(){
            head = nullptr;
            linkedList = nullptr;
            size = 0;
        }
        int pop(){
            if(size == 0){
                throw  "La pila e' vuota!!";
            }
            node *tmp = new node;
            tmp->prevNode = head->prevNode;
            tmp->value = head->value;
            size--;
            if(size >0){
            head->prevNode= tmp->prevNode->prevNode;
            head->value = tmp->prevNode->value;
            }
            return tmp->value;
        }
        node *insert(int value){
            node *tmp = new node;
            tmp->value=value;
            if(size == 0){
                tmp->prevNode=nullptr;
                head = tmp;
                linkedList = tmp;
            } else {
                tmp->prevNode = linkedList;
                linkedList = tmp;
                head = tmp;
                
            }
            size++;
            return tmp;
        }
        int getHead(){
            if(nullptr == head){
                throw "Non ci sono elementi nella pila!!";
            }
            return head->value;
        }
        void print(){
            node *tmp = linkedList;    
            cout<<"Stampo la Pila:"<<endl;
            while (tmp != nullptr)
            {
                cout<<to_string(tmp->value)<<endl;
                tmp= tmp->prevNode;
            }
            cout<<"Fine, la pila ha: "+to_string(getSize())+" elementi!"<<endl;
        }
        int getSize(){
            return size;
        }
};


int main(){

    Pila pila = Pila();
    pila.insert(1);    
    pila.insert(2);
    pila.insert(3);
    pila.insert(4);
    pila.insert(5);
    pila.insert(6);
    pila.insert(7);
    pila.print();
    cout<<"Effettuo un pop togliendo l'elemento: "+to_string(pila.pop())<<endl<<"La pila ha: "+to_string(pila.getSize())+" elementi!";
    cout<<"L'elemento in cima alla pila e': "+to_string(pila.getHead())<<endl;
    return 0;
}