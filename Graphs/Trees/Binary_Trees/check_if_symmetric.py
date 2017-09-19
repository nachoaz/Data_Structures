# check_if_symmetric.py

"""
Insight: the tree rooted at r is symmetric if r's left subtree == r's right
subtree.
"""


def is_symmetric(tree):

    def check_sym(l_subtr_root, r_subtr_root):
        #  is symmetric if l's right subtree and r's left subtree are symmetric
        #  AND if l's left subtree and r's right subtree are symmetric
        if (l_subtr_root is None) and (r_subtr_root is None):  # both empty
            return True
        elif l_subtr_root and r_subtr_root:  # neither empty
            data_is_same = l_subtr_root.data == r_subtr_root.data
            ls_r_and_rs_l_sym = check_sym(l_subtr_root.right, r_subtr_root.left)
            ls_l_and_rs_r_sym = check_sym(l_subtr_root.left, r_subtr_root.right)
            return data_is_same and ls_r_and_rs_l_sym and ls_l_and_rs_r_sym
        else:  # both empty
            return False

    return tree.root is None or check_sym(tree.left, tree.right)
