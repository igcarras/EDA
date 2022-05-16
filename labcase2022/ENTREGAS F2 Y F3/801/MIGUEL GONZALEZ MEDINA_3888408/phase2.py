# from binarysearchtree import BinarySearchTree
from tokenize import Number
from bst import BinarySearchTree
from bst import BinaryNode


class AVLTree(BinarySearchTree):

    # Override insert method from base class to keep it as AVL
    def insert(self, elem: object) -> None:
        """inserts a new node, with key and element elem"""
        self._root=self._insert(self._root,elem)

    def _insert(self, node: BinaryNode, elem: object) -> BinaryNode:
        """gets a node, searches the place to insert a new node with element e (using super()._insert),  and then,
        the function has to balance the node returned by the function super.()_insert"""
        # print("primero",node,elem)
        node = super()._insert(node, elem)
        # tree.draw()
        # print("segundo",node,elem)
        print("REBALANCE",node,elem)
        self.draw()
        node = self._rebalance(node)
        print("node: ",node,"RETURNING FROM ROTATE LEFT")
        # self.draw()
        # print("returning ",node)
        return node

    # Override remove method from base class to keep it as AVL
    def remove(self, elem: object) -> None:
        self._root = self._remove(self._root, elem)

    def _remove(self, node: BinaryNode, elem: object) -> BinaryNode:
        """ gets a node, searches the node with element elem in the subtree that hangs down node , and
        then remove this node (using super()._remove). After this, the function has to balance the node returned by the function super()._remove"""
        node = super()._remove(node, elem)
        print("AQUIII",node)
        self.draw()
        node = self._rebalance(node)
        return node

    def _rebalance(self, node: BinaryNode) -> BinaryNode:
        """ gets node and balances it"""
        # self.draw()
        if(not node):
            return
        if(node.left ==None and node.right==None or not node): 
            return node
        efactor = self.getEquilibriumFactor(node)
        parent = self.getParent(node.elem)
        #Getting parent side
        parentSide=self._getSide(parent,node)
       
        if(efactor>1):
            if(self.getEquilibriumFactor(node.right)==-1):
                #RotateRight + RotateLeft
                print("RotateRight + RotateLeft")
                self.rotateRight(node.right,node,"right")
                return self.rotateLeft(node,parent,parentSide)
            #rotateLeft
            return self.rotateLeft(node,parent,parentSide)
        if(efactor<-1):
            if(self.getEquilibriumFactor(node.left)==1):
                #RotateLeft + RotateRight
                print("RotateLeft + RotateRight")
                self.draw()
                self.rotateLeft(node.left,node,"left")
                self.draw()
                return self.rotateRight(node,parent,parentSide)
            #rotateRight
            return self.rotateRight(node,parent,parentSide)
            ...
        #efactor=0 or efactor=1
        print("node is balanced")
        return node

        
    def getEquilibriumFactor(self,node):
        return self._height(node.right) - self._height(node.left)

    def rotateRight(self,node,parent,parentSide):
        print("ROTATERIGHT",node)
        saved= node.left.right
        node.left.right = node
        if (not parent):
            self._root=node.left
            node.left = saved
            return self._root 
        else:
            setattr(parent,parentSide,node.left)
            node.left = saved
            self.draw()
            return getattr(parent,parentSide)

    def rotateLeft(self,node,parent,parentSide):
        print("ROTATELEFT",node)
        saved= node.right.left
        node.right.left = node
        if (not parent):
            self._root=node.right
            node.right = saved
            return self._root 
        else:
            setattr(parent,parentSide,node.right)
            node.right = saved
            return getattr(parent,parentSide)
        
    def getParent(self,elem):
    #    print("83: ",elem)
       if(not self._root):
           print("we are in root so no parent")
           return 
       return self._getParent(self._root,elem,None)

    def _getParent(self,node,elem,parent):
        # print("90: ",node,elem)
        if(node.elem==elem):
            return parent
        if(node.elem>elem):
            return self._getParent(node.left,elem,node)
        else:
           return self._getParent(node.right,elem,node)
    def _getSide(self,parent,node):
        if(parent !=None and parent.left== node):
            return "left"
        return "right"

        


# , 5, 15, 20, 24,25
tree = AVLTree()
for x in [50,11,34,5,3,4554,44,33,22,12,34,57,54]:
    tree.insert(x)
    # print("DEF")
    # tree.draw()
print("INSERT")
tree.draw()
print("REMOVE")
tree.remove(22)
tree.draw()
for x in [18, 11, 23, 5, 15, 20, 24,25]:
    nodito = tree.search(x)
    # print(nodito.elem,"--",tree.getEquilibriumFactor(nodito))

# tree.insert(40)
#factor de equilibrio
#detectar si nodo está desequilibrado recursivamente hacia arriba
#Si esta desequilibrado pillamos el que este y el children y aplicamos el case
    #CASE DE 4  
        # -rotateLeft
        # -rotateRight
        # -leftRight
        # -rightLeft



##LLLamar a isbalance
##luego los ifs
