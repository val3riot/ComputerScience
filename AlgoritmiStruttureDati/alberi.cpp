#include <iostream>
using namespace std;


struct node{
    int key;
    string value;
    node *preVal;
    node *leftC;
    node *rightC;
};
class Coda{

    private:
        node *lastValue, *head;
        int size;
    public:
        void insert(node *newNode){
            node *tmp = newNode;
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
        node *dequeue(){
            if(size == 0){
                throw "La coda e' vuota!";
            }
            node *tmp = new node;
            tmp->value=head->value;
            tmp->preVal=head->preVal;
            tmp->leftC=head->leftC;
            tmp->rightC=head->rightC;
            head = head->preVal;
            size --;
            return tmp;
        }
        string getHead(){
            if(nullptr == head){
                throw "Non ci sono elementi nella coda!!";
            }
            return head->value;
        }
        string getLastValue(){
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
                cout<<tmp->value<<endl;
                tmp= tmp->preVal;
            }
            cout<<"Fine, la coda ha: "+to_string(getSize())+" elementi!"<<endl;
        }
        int getSize(){
            return size;
        }
};


class BST{
    private:
        node *radice;
    public:
        BST(){
            radice = nullptr;
        }
        string search(int key){
            node *tmp = radice;
            while(tmp != nullptr){
                if(key == tmp->key){
                    return tmp->value;
                }else if(key<tmp->key){
                    tmp = tmp->leftC;
                } else{
                    tmp = tmp->rightC;
                }
            }
             return "Elemento non trovato!";
        }

        void insert(int key, string value){
            node *newNode = new node;
            node *tmp = radice;
            node *father = radice;
            newNode->key = key;
            newNode->value = value;
            newNode->leftC = nullptr;
            newNode->rightC = nullptr;
            newNode->preVal = nullptr;
            if(radice == nullptr){
                radice = newNode;

                return;
            }
            while(tmp != nullptr){
                father = tmp;
                if(key<=tmp->key){
                    tmp = tmp->leftC;
                } else{
                    tmp = tmp->rightC;
                }
            }
            if(key<=father->key){
                father->leftC = newNode;
            } else{
                father->rightC = newNode;
            }
        }
        void visitaDFS(){
            cout<<"Visita DFS: "<<endl;
            visitaDFSRicorsiva(radice);
        }
        void visitaDFSRicorsiva(node *nodo){
            if(nullptr != nodo){
                cout<<nodo->value<<endl;
                visitaDFSRicorsiva(nodo->leftC);
                visitaDFSRicorsiva(nodo->rightC);
            }
        }
        void visitaBFS(){
            cout<<"Visita BFS: "<<endl;
            Coda coda = Coda();
            coda.insert(radice);
            while(coda.getSize()>0){
                node *u = coda.dequeue();
                cout<<u->value<<endl;
                if(u->leftC!=nullptr && NULL !=u->leftC){
                    coda.insert(u->leftC);
                }
                if(u->rightC!=nullptr && NULL !=u->rightC){
                    coda.insert(u->rightC);   
                }
                
            }
        }
};





int main(){
    BST bst = BST();
    // for(int i = 0; i<20;i++){
    //     bst.insert(i,to_string(i));
    // }
    bst.insert(11,"A");
    bst.insert(8,"L");
    bst.insert(12,"B");
    bst.insert(7,"E");
    bst.insert(9,"R");
    bst.insert(13,"O");
    int key = 5;
    cout<<"Cerco l'elemento con chiave "+to_string(key)+": "+bst.search(key)<<endl;
    bst.visitaDFS();
    bst.visitaBFS();
    return 0;
}