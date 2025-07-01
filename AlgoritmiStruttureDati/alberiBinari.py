#------------ constants start --------------------------       
COUNT = [10]
#------------ constants end --------------------------       

#------------ Node declaration start  --------------------------       
class Node(object):
    def __init__(self, object):
        self.value = object
        self.left = None
        self.right = None
    def addChild(self, child):  
        if(child.value >= self.value):
            self.right = child
        else:
            self.left = child
    def printNode(self):
        node = self.value
        left = self.left.value if None != self.left else None
        right = self.right.value if None != self.right else None
        print(f"valore nodo: {node};\n\t valore figlio sinistra: {left};\n\t valore figlio destra: {right}")
#------------ Node declaration end --------------------------       

#------------ insert bst start --------------------------       
def insertTree(node, value):  
    if(node is None):
        return Node(value)
    if(node.value == value):
        print("Valore esistente")
        return
    if(value > node.value):
        node.right = insertTree(node.right, value)
    else:
        node.left =  insertTree(node.left, value)
    return node
#------------ insert bst end --------------------------       


#------------ visite DFS start --------------------------       
def visitaDFSRicorsiva(node, padreValue):
    print("-------------------\nVisita DFS Ricorsiva:\n")
    if(node is None):
        return
    print(f"valorePadre {padreValue} ---- valoreFiglio {node.value}")
    visitaDFSRicorsiva(node.left, node.value)
    visitaDFSRicorsiva(node.right, node.value)
def visitaDFS(node):
    print("-------------------\nVisita DFS:\n")
    s = []
    s.append(node)
    while len(s)>0:
        u = s.pop()
        if u is not None:
            print(u.value)
            s.append(u.left)
            s.append(u.right)   
#------------ visite DFS end --------------------------       

#------------ print 2d start --------------------------       
def print2DUtil(root, space):
 
    # Base case
    if (root == None):
        return
 
    # Increase distance between levels
    space += COUNT[0]
 
    # Process right child first
    print2DUtil(root.right, space)
 
    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(root.value)
 
    # Process left child
    print2DUtil(root.left, space)
# Wrapper over print2DUtil()
def print2D(root):
    print("-------------------\nPrint albero usando dfs ricorsiva:\n")

    # space=[0]
    # Pass initial space count as 0
    print2DUtil(root, 0)
#------------ print 2d end --------------------------       

#------------ visita BFS start --------------------------       
def visitaBFS(node):
    print("-------------------\nVisita BFS:\n")
    c = []
    c.append(node)
    while len(c)>0:
        u = c.pop(0)
        if u is not None:
            print(u.value)
            c.append(u.left)
            c.append(u.right)
#------------ visita BFS end--------------------------       

#--------------------------------------------------
#--------------------------------------------------
#------------ main start --------------------------       
def main():
    a = Node(9)
    value = [6,11,10,12,4,7]
    for i in value:
        insertTree(a,i)
    visitaDFS(a)
    #visitaDFSRicorsiva(a, None)
    visitaBFS(a)
    print2D(a)
if __name__ == "__main__":
    main()
#------------ main end --------------------------       
