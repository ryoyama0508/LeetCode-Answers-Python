# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def quickSort(self, nums):
        if len(nums) == 1:
            return nums
        povit = 0

        if len(nums) == 2 and nums[0] == nums[1]:
            return nums
        if nums[0] < nums[1]:
            povit = nums[1]
        else:
            povit = nums[0]

        newNums1 = []
        newNums2 = []
        for num in nums:
            if num < povit:
                newNums1.append(num)
            else:
                newNums2.append(num)

        return self.quickSort(newNums1)+self.quickSort(newNums2)


node = ListNode(0)
print(node)
print(node.val)
print(node.next)
