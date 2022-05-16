#Jorge Ramos Santana 100451001
#Marina Perez Barbero 100472115


from bst import BinarySearchTree
from bst import BinaryNode


class AVLTree(BinarySearchTree):

    # Override insert method from base class to keep it as AVL
    def insert(self, elem: object) -> None:
        """inserts a new node, with key and element elem"""
        self._root = self._insert(self._root, elem)

    def _insert(self, node: BinaryNode, elem: object) -> BinaryNode:
        """gets a node, searches the place to insert a new node with element e (using super()._insert),  and then,
        the function has to balance the node returned by the function super.()_insert"""
        node = super()._insert(node, elem)
        print("ELEM insert, ", node)
        node = self._rebalance(node)
        return node

    # Override remove method from base class to keep it as AVL
    def remove(self, elem: object) -> None:
        self._root = self._remove(self._root, elem)

    def _remove(self, node: BinaryNode, elem: object) -> BinaryNode:
        """ gets a node, searches the node with element elem in the subtree that hangs down node , and
        then remove this node (using super()._remove). After this, the function has to balance the node returned by the function super()._remove"""
        node = super()._remove(node, elem)
        print("Elem remove", node)
        node = self._rebalance(node)
        return node

    def RSD(self,node):
        x = node
        y = node.left
        x.left = y.right
        y.right = x
        return y

    def RSI(self,node):
        x = node
        y = node.right
        x.right = y.left
        y.left = x
        return y

    def RDDI(self,node):
        #self.draw()
        #x = node
        y = node.right
        z = y.left
        y.left = None
        node.right = z
        node.right.right = y
        return self.RSI(node)

    def RSID(self,node):
        #self.draw()
        #x = node
        y = node.left
        z = y.right
        y.right = None
        node.left = z
        node.left.left = y
        return self.RSD(node)


    def balance(self, node: BinaryNode) -> BinaryNode:  # calcula el factor de balance DEL NODO ACTUAL
        if node is None:
            return 0
        else:
            return self._height(node.left) - self._height(node.right)
            # aplicar formula del balance (Altura subarbol izquierdo - altura subarbol derecho)



    def _rebalance(self, node: BinaryNode) -> BinaryNode:

        balance = self.balance(node)  # calcula el factor de balance

        print("BALANCE", balance)

        if balance < -1:
            if node.right.right:
                # left rotation
                print("L Rotation")
                return self.RSI(node)

            elif node.right.left:
                # right-left rotation
                print("RL Rotation")
                return self.RDDI(node)

        elif balance > 1:
            if node.left.left:
                # right rotation
                print("R Rotation")
                return self.RSD(node)

            elif node.left.right:
                # left-right rotation
                print("LR Rotation")
                return self.RSID(node)
        else:
            return node  # no hace falta balancear


aux = AVLTree()
uno = [5, 3, 6, 4, 2, 1]
dos = [15, 6, 71, 4, 50, 7, 75, 3, 1]
tres = [32, 18, 92, 4, 70, 19, 95, 94, 96, 97]
cuatro = [50, 40, 60, 15, 65, 45, 63]
cinco = [15, 6, 50, 4, 23, 71, 5]
seis = [15, 6, 50, 4, 7, 23, 71, 5]
siete = [12, 6, 18, 8, 20, 14, 4, 2]
ocho = [12, 8, 17, 6, 16, 19, 20]
nueve = [3, 2, 5, 4, 6]
for x in nueve:
    aux.insert(x)
    aux.draw()
    print("-----")
aux.draw()
aux.remove(2)
aux.draw()
