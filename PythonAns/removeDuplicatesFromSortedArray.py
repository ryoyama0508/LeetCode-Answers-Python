class Solution(object):
    """
    took from discussion but still solved
    it was slow af
    """

    def removeDuplicates(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not A:
            return 0

        newTail = 0

        for i in range(1, len(A)):
            if A[i] != A[newTail]:
                newTail += 1
                A[newTail] = A[i]

        return newTail + 1
