class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def clone_with_offset(self, node: TreeNode, offset):

        if not node:
            return None

        else:

            # Clone whole tree with constant value offset
            root_node = TreeNode(node.val + offset)
            root_node.left = self.clone_with_offset(node.left, offset)
            root_node.right = self.clone_with_offset(node.right, offset)

            return root_node

    def generateTrees(self, n: int):

        if n == 0:
            # Quick response for empty tree
            return []

        # dynamic programming table
        bst_dp_table = [None for i in range(n + 1)]

        # base case:
        bst_dp_table[0] = [None]

        # bottom-up. build bst with k nodes, k from 1 to n
        for number_of_nodes in range(1, n + 1):

            bst_dp_table[number_of_nodes] = []

            # for root node of bst:     1 node
            # for left-subtree of bst : (number_of_nodes_on_left) nodes
            # for right-subtrr of bst : (k-1-number_of_nodes_on_left) nodes
            for number_of_nodes_on_left in range(0, number_of_nodes):

                for left_subtree in bst_dp_table[number_of_nodes_on_left]:

                    number_of_nodes_on_right = (
                        number_of_nodes - 1 - number_of_nodes_on_left
                    )

                    for right_subtree in bst_dp_table[number_of_nodes_on_right]:

                        # construct one unique bst
                        root_of_bst = TreeNode(number_of_nodes_on_left + 1)
                        root_of_bst.left = left_subtree
                        root_of_bst.right = self.clone_with_offset(
                            right_subtree, number_of_nodes_on_left + 1
                        )

                        # update dynamic programming table
                        bst_dp_table[number_of_nodes].append(root_of_bst)

        return bst_dp_table[n]


# [[None], [TreeNode{val: 1, left: None, right: None}], [TreeNode{val: 1, left: None, right: TreeNode{val: 2, left: None, right: None}}, TreeNode{val: 2, left: TreeNode{val: 1, left: None, right: None}, right: None}], None]

# [[None], [TreeNode{val: 1, left: None, right: None}], [TreeNode{val: 1, left: None, right: TreeNode{val: 2, left: None, right: None}}, TreeNode{val: 2, left: TreeNode{val: 1, left: None, right: None}, right: None}], [TreeNode{val: 1, left: None, right: TreeNode{val: 2, left: None, right: TreeNode{val: 3, left: None, right: None}}}, TreeNode{val: 1, left: None, right: TreeNode{val: 3, left: TreeNode{val: 2, left: None, right: None}, right: None}}, TreeNode{val: 2, left: TreeNode{val: 1, left: None, right: None}, right: TreeNode{val: 3, left: None, right: None}}, TreeNode{val: 3, left: TreeNode{val: 1, left: None, right: TreeNode{val: 2, left: None, right: None}}, right: None}, TreeNode{val: 3, left: TreeNode{val: 2, left: TreeNode{val: 1, left: None, right: None}, right: None}, right: None}]]