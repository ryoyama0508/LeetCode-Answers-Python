# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":
        if root is None:
            return None
        self.nodes = [[root]]
        self.store(root.left, 1)
        self.store(root.right, 1)

        for same_lev_nodes in self.nodes:
            for i in range(len(same_lev_nodes)):
                if i == len(same_lev_nodes) - 1:
                    same_lev_nodes[i].next = None
                    continue
                same_lev_nodes[i].next = same_lev_nodes[i + 1]
        return root

    def store(self, root, level):
        if root is None:
            return

        if len(self.nodes) < level + 1:
            self.nodes.append([])
        self.nodes[level].append(root)

        self.store(root.left, level + 1)
        self.store(root.right, level + 1)
