#Examne junio 2020
from slist import SList
class Node:
    def __init__(self , elem):
        self.elem = elem
        self.right = None
        self.left = None

class MyBST:
    def __init__(self):
        self._root = None

    def depth(self, node):
        """ returns the depth of the node; this is the length from
        the root to the node"""
        depth_level = None

        if self._root is None:
            print('Error: the tree is empty')
        else:
            # we can use SList with tail and head
            depth_level = 0

            list_nodes = SList()
            list_nodes.addLast(self._root)

            while len(list_nodes) > 0:  # loop will be executed the size of tree: n
                current = list_nodes.removeFirst()  # O(1)
                if current == node:
                    return depth_level
                if current.left is not None and node.elem<current.elem:
                    list_nodes.addLast(current.left)  # O(1)
                if current.right is not None and node.elem>current.elem:
                    list_nodes.addLast(current.right)  # O(1)
                depth_level += 1

        print('Not found ', node.elem)
        return None

    def height(self) -> int:
        """Returns the height of the tree"""
        return self._height(self._root)

    def _height(self, node: Node) -> int:
        """return the height of node"""
        if node is None:
            return -1
        else:
            return 1 + max(self._height(node.left), self._height(node.right))


    def search(self, elem:object):
        return self._search(self._root, elem)

    def _search(self,node, elem):

        if node is None or node.elem == elem:
            return node

        elif elem < node.elem:
            return self._search(node.left, elem)
        elif elem > node.elem:
            return self._search(node.right, elem)

    def insert(self, elem: object) -> None:
        self._root = self._insert(self._root, elem)

    def _insert(self, node: Node, elem: object) -> Node:
        if node is None:
            return Node(elem)

        if node.elem == elem:
            print('Error: elem already exist ', elem)
            return node

        if elem < node.elem:
            node.left = self._insert(node.left, elem)
        else:
            # elem>node.elem
            node.right = self._insert(node.right, elem)
        return node

    def draw(self) -> None:
        """function to draw a tree. """
        if self._root:
            self._draw('', self._root, False)
        else:
            print('tree is empty')
        print('\n\n')

    def _draw(self, prefix: str, node: Node, is_left: bool) -> None:
        if node is not None:
            self._draw(prefix + "     ", node.right, False)
            print(prefix + "|-- " + str(node.elem))
            self._draw(prefix + "     ", node.left, True)

    def padre(self, elem) -> int:
        return self._padre(self._root, elem)

    def _padre(self, node: Node, elem: object) -> Node:
        if node is None or self._search(self._root, elem) is None:
            print("Nodo",elem, "no existe")
            return None

        if node.left.elem == elem or node.right.elem == elem:
            return node.elem

        elif elem < node.elem:
            return self._padre(node.left, elem)
        elif elem > node.elem:
            return self._padre(node.right, elem)


    def checkCousins(self, x, y):
        X = self.search(x)
        Y = self.search(y)

        if X == None or Y == None:
            print("No existe")
            return False

        prof_a = self.depth(X)
        prof_b = self.depth(Y)

        print("profundidad de x", X.elem , prof_a)
        print("profundidad de y", Y.elem,  prof_b)

        padre_x = self.padre(x)
        padre_y = self.padre(y)
        print("padre de x", padre_x)
        print("padre de y", padre_y)


        abuelo_x = self.padre(padre_x)
        abuelo_y = self.padre(padre_y)
        print("abuelo de x", abuelo_x)
        print("abuelo de y", abuelo_y)

        if prof_a != prof_b:
            print("Altura diferente")
            return False

        if padre_x == padre_y:
            print("Mismo padre")
            return False

        if abuelo_x != abuelo_y:
            print("Distinto abuelo")
            return False
        return True





values=[25,20,36,10,22,30,40,5,12,28,38,48]
tree=MyBST()
for x in values:
    tree.insert(x)

tree.draw()


print('5 and 15 are cousins?:', tree.checkCousins(5,15)) #False, 15 does not exist
print('5 and 22 are cousins?:', tree.checkCousins(5,22)) #False, have diferent levels
print('5 and 22 are cousins?:',tree.checkCousins(5,22)) #False, have diferent levels
print('36 and 48 are cousins?:',tree.checkCousins(36,48)) #False, have diferent levels
print('5 and 12 are cousins?:',tree.checkCousins(5,12)) #False, are siblings
print('20 and 36 are cousins?:',tree.checkCousins(20,36)) #False, are siblings
print('10 and 22 are cousins?:',tree.checkCousins(10,22)) #False, are siblings
print('5 and 28 are cousins?:',tree.checkCousins(5,28)) #False, same level, their parents are not siblings
print('12 and 28 are cousins?:',tree.checkCousins(12,28)) #False, same level, their parents are not siblings
print('10 and 30 are cousins?:',tree.checkCousins(10,30)) #True, are cousins
print('10 and 40 are cousins?:',tree.checkCousins(10,30)) #True, are cousins
print('22 and 30 are cousins?:',tree.checkCousins(22,30)) #True, are cousins
print('22 and 40 are cousins?:',tree.checkCousins(22,40)) #True, are cousins
print('28 and 38 are cousins?:',tree.checkCousins(28,38)) #True, are cousins
print('28 and 48 are cousins?:',tree.checkCousins(28,48))  #True, are cousins
print('28 and 48 are cousins?:',tree.checkCousins(28, 48))  # True, are cousins
nodo = tree.search(5)
print("Profundidad nodo 5:", tree.depth(nodo))