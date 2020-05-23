class Solution(object):
    """ わからんのでまた後でreview """

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        """ Use a variable prevSum to record the sum of all node values from the root r to the parent p of the current node. """
        def dfs(root, prevSum, sum):
            if not root:
                return
            """ Then including the current node, the sum becomes currSum = prevSum + node.val. """
            currSum = prevSum + root.val
            """ Now for each node on the path, we can calculate their respective currSum """

            """ If the sum of nodes on a path ending with the current node has value sum, it implies that currSum - sum is in rec """
            if currSum - sum in rec:

                self.count += rec[currSum - sum]
            if currSum in rec:
                rec[currSum] += 1
            else:
                """ we use a dictionary rec to record the frequency of all such sums.  """
                rec[currSum] = 1
            dfs(root.left, currSum, sum)
            dfs(root.right, currSum, sum)
            rec[currSum] -= 1

        self.count = 0
        rec = {0: 1}
        dfs(root, 0, sum)
        return self.count
