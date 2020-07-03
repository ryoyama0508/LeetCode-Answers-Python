class Solution(object):
    def canJump(self, nums):
        if nums[0] == 0:
            if len(nums) == 1:
                return True
            else:
                return False
        for i in range(0, len(nums)-1):
            if nums[i] == 0:
                c = 1
                check = True
                for j in range(i-1, -1, -1):
                    if nums[j] > c:
                        check = True
                        break
                    else:
                        check = False
                    c += 1
                if check == False:
                    return False

        return True
