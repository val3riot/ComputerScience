#include <iostream>
using namespace std;


struct node{
    node *preVal;
    int value;
};

class Coda{

    private:
        node *lastValue, *head;
        int size;
    public:
        void insert(int value){
            node *tmp = new node;
            tmp->value = value;
            tmp->preVal = nullptr;
            if(size == 0){
                head = tmp;
                lastValue = tmp;
            } else {
                lastValue->preVal = tmp;
                lastValue = tmp;
            }
            size ++;
        }
        int dequeue(){
            if(size == 0){
                throw "La coda e' vuota!";
            }
            int tmp = head->value;
            head = head->preVal;
            size --;
            return tmp;
        }
        int getHead(){
            if(nullptr == head){
                throw "Non ci sono elementi nella coda!!";
            }
            return head->value;
        }
        int getLastValue(){
            if(nullptr == head){
                throw "Non ci sono elementi nella coda!!";
            }
            return lastValue->value;
        }
        void print(){
            node *tmp = head;    
            cout<<"Stampo la coda:"<<endl;
            while (tmp != nullptr)
            {
                cout<<to_string(tmp->value)<<endl;
                tmp= tmp->preVal;
            }
            cout<<"Fine, la coda ha: "+to_string(getSize())+" elementi!"<<endl;
        }
        int getSize(){
            return size;
        }
};



int main(){

    Coda coda = Coda();
    coda.insert(1);    
    coda.insert(2);
    coda.insert(3);
    coda.insert(4);
    coda.insert(5);
    coda.insert(6);
    coda.insert(7);
    coda.print();
    cout<<"Effettuo un pop togliendo l'elemento: "+to_string(coda.dequeue())<<endl<<"La coda ha: "+to_string(coda.getSize())+" elementi!";;
    cout<<"L'elemento in cima alla coda e': "+to_string(coda.getHead())<<endl;
    cout<<"L'elemento in fondo alla coda e': "+to_string(coda.getLastValue())<<endl;
    return 0;
}