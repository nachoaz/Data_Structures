# check_if_height_balanced.py

"""
Given a binary tree, check if it's height-balanced. (A binary tree is said to
be height-balanced if for each node in the tree, the difference in the height of
its left and right subtrees is at most one.
"""


from collections import namedtuple


def is_balanced(tree):

    BalancedStatusWithHeight = namedtuple('BalancedStatusWithHeight',
                                          ('balanced', 'height'))

    def check_subtree_balanced(subtree_root):
        """Checks if subtree rooted at subtree_root is height-balanced."""

        if subtree_root is None:
            return BalancedStatusWithHeight(True, -1)

        left_result = check_subtree_balanced(subtree_root.left)
        if not left_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        right_result = check_subtree_balanced(subtree_root.right)
        if not right_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)

    return check_subtree_balanced(tree.root).balanced
