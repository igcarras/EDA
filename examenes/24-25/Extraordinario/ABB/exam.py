from slistH import SList
from slistH import SNode
from bintree import BinaryNode
from bst import BinarySearchTree
class MyBST (BinarySearchTree):
    def even_elements_inorder(self) -> SList:
        list_bst = SList()
        self._even_elements_inorder(self._root, list_bst)
        return list_bst

    def _even_elements_inorder(self, node: BinaryNode, list_bst: SList) -> None:
            if node is None:
                return None
            self._even_elements_inorder(node.left, list_bst)
            if node.elem % 2 == 0:
                list_bst.addLast(node.elem)
            self._even_elements_inorder(node.right, list_bst)
            return

    def print_reverse_slist(self, node:SNode):
        """Imprime los elementos desde el final al inicio usando recursión"""
        if node is None:
            return
        self.print_reverse_slist(node.next)
        print(node.elem, end=' ')




if __name__ == "__main__":
    # Ejemplo de uso:
    tree = MyBST()

    for val in [10, 5, 3, 7, 20, 15, 30, 8, 6]:
        tree.insert(val)

    result = SList()
    result = tree.even_elements_inorder()
    print(result)
    tree.print_reverse_slist(result._head)