# -*- coding: utf-8 -*-

from binarysearchtree import BinarySearchTree

class BST(BinarySearchTree):

    def countPairs(self,otherTree,k):
        if otherTree==None:
            return 0

        if self._root==None:
            return 0

        return self._countPairs(self._root,otherTree,k)
        
    def _countPairs(self, node, otherTree, k):
        if node==None:
            return 0

        result=0
        if otherTree.find(k-node.key):
            #si el otro árbol contiene una key igual a x-node.key, eso significa, que
            #ya hemos encontrado un par
            result=1
            
        #ahora tendremos que seguir buscando pares por la izquierda y por la derecha    
        result+=self._countPairs(node.left,otherTree,k)+self._countPairs(node.right,otherTree,k)
        return result



if __name__=='__main__':
    tree1=BST()
    tree2=BST()

    data1=[5,3,7,2,4,6,8,10,11,13,9,1,0,]
    data2=[10,6,15,3,8,11,18,1,2,5,4,9,7,13]

    for i in data1:
        tree1.insert(i,i)

    for i in data2:
        tree2.insert(i,i)

    tree1.draw(False)

    print('.................')

    tree2.draw(False)


    print('................')    

    print(tree1.countPairs(tree2,20))

