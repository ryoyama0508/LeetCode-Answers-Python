from collections import defaultdict


class TreeNode(object):
    def __init__(self):
        # ()inside!! default value
        self.dic = defaultdict(TreeNode)
        self.stop = False


class Trie(object):

    def __init__(self):
        self.tree = TreeNode()

    def insert(self, word):
        nowNode = self.tree
        for c in word:
            if c not in nowNode.dic:
                nowNode.dic[c] = TreeNode()
            nowNode = nowNode.dic[c]
        nowNode.stop = True

    def search(self, word):
        nowNode = self.tree
        for c in word:
            if c in nowNode.dic:
                nowNode = nowNode.dic[c]
            else:
                return False
        return nowNode.stop

    def startsWith(self, prefix):
        nowNode = self.tree
        for c in prefix:
            if c in nowNode.dic:
                nowNode = nowNode.dic[c]
            else:
                return False
        return True
