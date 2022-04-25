# -*- coding: utf-8 -*-
#MARÍA CAMPOS CARNEROS#
class BinaryNode:
    def __init__(self, elem: int, node_left: 'BinaryNode' = None, node_right: 'BinaryNode' = None) -> None:
        self.elem = elem
        self.left = node_left
        self.right = node_right


class MyBinarySearchTree:
    def __init__(self) -> None:
        """creates an empty binary tree
        I only has an attribute: _root"""
        self._root = None

    def draw(self) -> None:
        """function to draw a tree. """
        if self._root:
            self._draw('', self._root, False)
        else:
            print('tree is empty')
        print('\n\n')

    def _draw(self, prefix: str, node: BinaryNode, is_left: bool) -> None:
        if node is not None:
            self._draw(prefix + "     ", node.right, False)
            print(prefix + "|-- " + str(node.elem))
            self._draw(prefix + "     ", node.left, True)

    def insert(self, elem: object) -> None:
        self._root = self._insert(self._root, elem)

    def _insert(self, node: BinaryNode, elem: object) -> BinaryNode:
        if node is None:
            return BinaryNode(elem)

        if node.elem == elem:
            print('Error: elem already exist ', elem)
            return node

        if elem < node.elem:
            node.left = self._insert(node.left, elem)
        else:
            # elem>node.elem
            node.right = self._insert(node.right, elem)
        return node

  # Removes all leaf nodes having value inside the given range
  # returns a sorted list in descending order
    def removeInsideRange(self, min: int, max: int):
        if self._root is None:
            return []
         
        lista=[]
        self._removeInsideRange(self._root,min,max,lista)
        return lista
    
    def _removeInsideRange(self, node,max:int, min:int,lista):
        #Para que aparezca en orden descendente se tiene que recorrer el árbol visitando primero el hijo derecho, después el nodo, y por último y le hijo izquierdo
        if node is None:
            return []

        if min<0 or max<0:
            return []
        
        if min==max:
            return []
        
        if self._size(node)==1 and min<=node.elem<=max:
            lista.appen(node.elem)
        if self._size(node)==1 and node.elem<min:
            return []
        if self._size(node)==1 and node.elem<max:
            return []
        


       
    
        self._removeInsideRange(node.right,max,min,lista)
        if min<=node.elem<=max and node.right is None and node.left is None:
            lista.append(node.elem)
        self._removeInsideRange(node.left,max, min,lista)
                
    def size(self):
        return self.size(self._root)
    def _size(self, node:BinaryNode):
        if node is None:
            return 0
        else:
            return 1 + self._size(node.left) + self._size(node.right)
            





if __name__ == "__main__":

    aux = MyBinarySearchTree()
    for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
        aux.insert(x)
    print("Original Tree")
    aux.draw()

    print("Remove leaf nodes in range: 1, 120")
    print("Nodes removed", aux.removeInsideRange(1,120))

    aux2 = MyBinarySearchTree()
    for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
        aux2.insert(x)


    print("Remove leaf nodes in range: 15, 20")
    print("Nodes removed", aux2.removeInsideRange(15,20))

    aux3 = MyBinarySearchTree()
    for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
        aux3.insert(x)


    print("Remove leaf nodes in range: 0, 0")
    print("Nodes removed", aux3.removeInsideRange(0,0))

    aux4 = MyBinarySearchTree()
    for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
        aux4.insert(x)


    print("Remove leaf nodes in range: 54, 80")
    print("Nodes removed", aux4.removeInsideRange(54,80))

    aux5 = MyBinarySearchTree()
    for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
        aux5.insert(x)

    print("Remove leaf nodes in range: -10, 0")
    print("Nodes removed", aux4.removeInsideRange(-10,0))