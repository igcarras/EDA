"""
Implement a Divide and Conquer function sorted_list_to_bst that converts a sorted singly linked list into 
a height-balanced Binary Search Tree (BST), without converting the list into an array. 
Function Specification Parameters: 
    sl: single linked list
    Return: the function returns a BinaryNode object representing the root of the constructed balanced BST.
    You must use the Divide and Conquer strategy; other strategies will not be considered.
    If you need to use any functions, you must implement them.
    What is the time complexity of the function? Justify your answer.
        The time complexity of the function is O(n log n), because each level of recursion costs O(n) 
        to find the middle, and there are O(log n) levels.
"""

from slistHT import SList
from bintree import BinaryNode, BinaryTree


def sorted_list_to_bst (sl: 'SList'):
     if sl._head is None:
        return None
     return _sorted_list_to_bst(sl._head, 0, len(sl)-1)
    
def _sorted_list_to_bst(head, start,end):
    # Base case, empty list
    if start > end:
            return None
    # 1. Find the middle node
    # Using n // 2 tells us exactly how many steps to take
    midNode = head
    mid = (start+end)//2
    for _ in range(mid):
        midNode = midNode.next

    # 2. Create the root for this sub-tree
    root = BinaryNode(midNode.elem)

    # 4. Recursive calls
    root.left = _sorted_list_to_bst(head, start, mid -1)
    root.right = _sorted_list_to_bst(head, mid +1, end)

    return root


sl = SList()
for x in [1, 2,3,4,5,6,7]:
    sl.add_last(x)
print(sl)
# --- Execution ---
tree = BinaryTree()

# FIXED: 
# 1. Pass dl._head (the node) instead of dl (the object)
# 2. Assign the result to tree._root so draw() has something to show
tree._root = sorted_list_to_bst(sl)

# FIXED: draw is a method, it needs parentheses
if tree._root:
    tree.draw()