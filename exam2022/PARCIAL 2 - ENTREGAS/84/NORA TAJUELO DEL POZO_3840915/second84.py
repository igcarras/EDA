# -*- coding: utf-8 -*-
#Nora Tajuelo del Pozo 
#grupo 84 
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

    # Removes all leaf nodes having value outside the given range
    # returns a sorted list in ascending order
    def removeOutsideRange(self, min: int, max: int) -> []:
        resultado = []
        #caso base: si el arbol no tiene ningún nodo 
        if self._root == None: 
            return []
        
        #llamamos a la funcion recursiva 
        self._removeOutsideRange(self._root,min, max, resultado)
        return resultado
    
    #debemos buscar solo aquellos nodos hoja, por eso utilizamos una funcion
    #auxiliar, que defina el numero de hijos de cada nodo 
    #si el nodo no tiene hijos, es una hoja 
    
    def num_hijos(self, node:"BinaryNode"): 
        contador = 0
        if node:
            if node.left:
                contador += 1
            if node.right:
                contador += 1
        return contador
    
    def delete(self,node:"BinaryNode"): 
        #si existe nodo comprobamos que tenga padre y lo desvinculamos 
        if node.parent != None: 
            nodo_auxiliar= node.parent
            if nodo_auxiliar.left: 
                node=nodo_auxiliar.left
                nodo_auxiliar.left = node
                node = None 
            if nodo_auxiliar.right: 
                node=nodo_auxiliar.right
                nodo_auxiliar.right = node
                node = None 
      
    def _removeOutsideRange(self, node:"BinaryNode", min, max, resultado): 
        if node: 
            #buscamos aquellos nodos que sean hojas 
            if self.num_hijos ==2:
                return [] 
            if self.num_hijos ==1: 
                return []
            else: 
                #en el resto de casos, solo puede tener 0 hijos, por lo que es 
                #una hoja 
                if self.node.elem>=min or self.node.elem<=max: 
                    resultado.append(node)
                    self.delete(node)
                    self._removeOutsideRange(self, node.left, min, max, resultado)
                self._removeOutsideRange(self, node.right, min, max, resultado)
            
        return resultado 
  
         
if __name__ == "__main__":
    tree = MyBinarySearchTree()
    for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
        tree.insert(x)

    print("Original Tree")
    tree.draw()

    tree = MyBinarySearchTree()
    for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
        tree.insert(x)
    print("Remove leaf nodes out range: 1, 120")
    print("Nodes removed", tree.removeOutsideRange(1,120))
    tree = MyBinarySearchTree()
    for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
        tree.insert(x)
    print("Remove leaf nodes out range: 15, 20")
    print("Nodes removed", tree.removeOutsideRange(15,20))
    tree = MyBinarySearchTree()
    for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
        tree.insert(x)
    print("Remove leaf nodes out range: 0, 0")
    print("Nodes removed", tree.removeOutsideRange(0,0))
    tree = MyBinarySearchTree()
    for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
        tree.insert(x)
    print("Remove leaf nodes out range: 9, 23")
    print("Nodes removed", tree.removeOutsideRange(9, 23))
    tree = MyBinarySearchTree()
    for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
        tree.insert(x)
    print("Remove leaf nodes out range: -10, 0")
    print("Nodes removed", tree.removeOutsideRange(-10, 0))
    tree = MyBinarySearchTree()
    for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
        tree.insert(x)
    print("Remove leaf nodes out range: 5, 80")
    print("Nodes removed", tree.removeOutsideRange(5, 80))
