# -*- coding: utf-8 -*-
"""
Test program comparing solutions with the builtin list-based one.

@author: EDA Team
"""

# Classes provided by EDA Team
from bst import BinarySearchTree
import unittest

# Classes containing the different solutions
import solution_with_builtin_types
import solution_with_iter
import solution_with_rec

"""
    Auxiliary functions to convert between types and more
"""


def __bst_as_str(bst: BinarySearchTree) -> str:
    top = 10
    lst = bst.inorder_list()
    if len(lst) > top:
        return str(lst[0:top])[0:-1] + ", ..."
    else:
        return str(lst)


class Test(unittest.TestCase):
    def setUp(self):
        ...

    def test_test01(self):
        ...


# Some usage examples
if __name__ == '__main__':
    unittest.main()
