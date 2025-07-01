class Node:
    def __init__(self,value,color):
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        pass
    def get_value(self):
        return (self.value,self.color)
class Albero:
    def __init__(self):
        self.radice = None
        pass
    def searchMaxRedPath(self,nodo):
        if nodo is None or nodo.color == 'B':
            return 0
        l = self.searchMaxRedPath(nodo.left)
        r = self.searchMaxRedPath(nodo.right)
        return nodo.value + max(l,r)

    def altezza(self,nodo):
        if nodo is None:
            return 0
        l = self.altezza(nodo.left)
        r = self.altezza(nodo.right)
        return 1 + max(l,r)
    def counte_altezze_h(self, nodo, h, c):
        if nodo is None:
            return 0
        res = 1 if c > h else 0
        c+=1
        l = self.counte_altezze_h(nodo.left,h,c)
        r = self.counte_altezze_h(nodo.right,h,c)
        return res + l + r
    def delta_antenati_discendenti(self, nodo, antenati):
        if nodo is None:
            return (0,0)
        l,cl = self.delta_antenati_discendenti(nodo.left,antenati + nodo.value)
        r,cr = self.delta_antenati_discendenti(nodo.right,antenati + nodo.value)
        c= 1 if antenati == l+r else 0
        return (nodo.value+l+r,c+cl+cr)
    def delta(self):
        _,c=self.delta_antenati_discendenti(self.radice,0)
        return c
    def print_tree(self,node, level=0):
        if node is None:
            return

        print("  " * level + f"- {node.value}")

        if node.left:
            self.print_tree(node.left, level + 1)
        if node.right:
            self.print_tree(node.right, level + 1)
    def stampa_albero(self):
        print('Albero: ')
        self.print_tree(self.radice)
    def ngf(self,nodo,min,alt):
        if nodo is None:
            return 0
        if min >nodo.value:
            min = nodo.value
        alt+=1
        l = self.ngf(nodo.left,min,alt)
        r = self.ngf(nodo.right,min,alt)
        v = 1 if alt > min else 0
        return l+r+v
    def nodi_generazionalmente_profondi(self):
        return self.ngf(self.radice,self.radice.value,0)
def esercizio1(): 
    radice = Node(1,'R')
    radice.left = Node(10,'R')
    radice.right = Node(4,'R')

    radice.left.left = Node(1,'R')
    radice.left.left.left = Node(1,'R')
    radice.left.left.right = Node(2,'R')

    radice.left.right = Node(2,'R')
    radice.left.right.left = Node(30,'B')
    radice.left.right.left.left = Node(50,'R')
    radice.left.right.right = Node(2,'R')

    radice.right.left = Node(15,'R')
    radice.right.right = Node(20,'B')
    radice.right.left.left = Node(2,'B')
    radice.right.right.left = Node(20,'R')
    albero = Albero()
    albero.radice = radice
    albero.stampa_albero()
    print('valore massimo di un percorso di nodi rossi: ',albero.searchMaxRedPath(albero.radice))
    print('Altezza albero: ',albero.altezza(albero.radice))
    print('Nodi con altezza superiore a 3: ',albero.counte_altezze_h(albero.radice,3,1))
def esercizio2():
    albero=Albero()
    radice = Node(2,'B')
    radice.left = Node(5,'B')
    radice.right = Node(3,'B')
    radice.left.left = Node(1,'B')
    radice.left.right = Node(1,'B')
    radice.right.left = Node (2,'B')
    radice.right.left.left = Node(4,'B')
    radice.right.left.right = Node(1,'B')
    albero.radice = radice
    albero.stampa_albero()
    print('Nodi Bilanciati: ',albero.delta())
    print('Nodi Generazionalmente profondi: ',albero.nodi_generazionalmente_profondi())


def main():
    #esercizio1()
    esercizio2()
if __name__=="__main__":
    main()