class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] = dic[num] + 1
            else:
                dic[num] = 1

        for i, v in dic.items():
            if v > (len(nums) / 2):
                return i


# Follow-up: Could you solve the problem in linear time and in O(1) space?


class SolutionFromDiscussion:
    # The algorithm first determines the frequency of each bit in the input array.
    # If there is a number with a majority in the input (i.e. it makes up more than half of the input),
    # then the frequency of all its set bits will be in the majority, and the frequency of all its unset bits will be in the minority.
    #
    # The majority number can be recreated from the frequency table by masking together all the majority bits.
    # This relies on there being a majority. If there is not guaranteed to be a majority a second pass to check the result is required.
    def majorityElement(self, nums):
        bitFrequencyTable = [0] * 32  # Bit frequency table

        #   Work out bit frequency
        for num in nums:
            for j in range(32):  #  for each bit
                if (num >> j & 1) != 0:  # is bit j set?
                    bitFrequencyTable[j] += 1  # increment frequency

        #  Recreate the majority number
        res = 0
        for i, val in enumerate(bitFrequencyTable):  # for each bit
            if val > len(nums) // 2:  # is bit i in the majority?
                if i == 31:  # if the 31th bit if 1, it means it's a negative number
                    res = -((1 << 31) - res)
                else:
                    res |= (
                        1 << i
                    )  # mask bit i into the result (insert and slide to add)
        return res
