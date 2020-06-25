class Solution(object):
    def maxArea(self, h):
        i = maxSF = 0
        j = len(h) - 1
        while i < j:
            if h[i] < h[j]:
                maxSF = max(maxSF, h[i]*(j-i))
                i += 1
            else:
                maxSF = max(maxSF, h[j]*(j-i))
                j -= 1

        return maxSF
