from slistH import SList
from slistH import SNode
from bintree import BinaryNode
from bst import BinarySearchTree


class MyList(SList):
    def print_reverse_slist(self):
        self._print_reverse_slist(self._head)
        return

    def _print_reverse_slist(self, node: SNode):
        """Imprime los elementos desde el final al inicio usando recursión"""
        if node is None:
            return
        self._print_reverse_slist(node.next)
        print(node.elem, end=' ')


class MyBST (BinarySearchTree):
    def even_elements(self) -> MyList:
        list_bst = MyList()
        self._even_elements(self._root, list_bst)
        return list_bst

    def _even_elements(self, node: BinaryNode, list_bst: SList) -> None:
            if node is None:
                return None
            self._even_elements(node.left, list_bst)
            if node.elem % 2 == 0:
                list_bst.addLast(node.elem)
            self._even_elements(node.right, list_bst)
            return




if __name__ == "__main__":
    # Ejemplo de uso:
    tree = MyBST()

    for val in [10, 5, 3, 7, 20, 15, 30, 8, 6]:
        tree.insert(val)

    result = tree.even_elements()
    print("Números pares del ABB:", "\n", result)

    tree2 = MyBST()
    for val in [12, 5, 3, 7, 1, 23, 4, 9, 2]:
        tree2.insert(val)

    result = tree2.even_elements()
    print("Números pares del ABB:", "\n", result)
