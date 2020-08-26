import math


class Solution:
    def numSquares(self, n: int) -> int:
        # Generate the squares, reverse to be in decreasing order for efficiency.
        sqrs = [i**2 for i in range(1, int(math.sqrt(n))+1)]
        print(sqrs)
        mins = float('inf')

        def helper(rest, nums, idx):
            nonlocal mins
            l = len(nums)
            print(nums, "nums")
            # If the current nums we're using >= the min that lead to the target return.
            # If rest < 0 or > n return.
            if l >= mins or rest < 0 or rest > n:
                return
                # If by this stage our t == 0 we store the l, this only gets update if l < mins.
            if rest == 0:
                mins = l
                return
            else:
                # Recursively work through the sqrs.
                for i in range(idx, len(sqrs)):
                    helper(rest - sqrs[i], nums + [sqrs[i]], i)

        helper(n, [], 0)
        return mins if mins != float('inf') else -1


obj = Solution()
print(obj.numSquares(13))
