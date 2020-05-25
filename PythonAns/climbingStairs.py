class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.climbRecursive(0, n)

    def climbRecursive(self, current, goal):
        if current > goal:
            return 0
        elif current == goal:
            return 1

        return self.climbRecursive(current + 1, goal) + self.climbRecursive(current + 2, goal)
        # time limit exceeded

    def climbLoop(self, n):
        d = []
        [0] * n
        d[0] = 0
        d[1] = 1
        i = 2
        for i, _ in enumerate(d):
            d[i] = d[i-1] + d[i - 2]
            i += 1
            if i > n:
                break

        return d[n]

    def recuriveMath(self, a, b, i, n):
        print(i)
        sam = 2 * a + (b-a)
        print("sam", sam)

        if i == n:
            return sam
        i += 1
        return self.recuriveMath(b, sam, i, n)
