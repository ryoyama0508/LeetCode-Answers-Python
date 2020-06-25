class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        ret = []
        for i in range(0, len(nums)-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    ret.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return ret


class WrongSolution(object):
    def threeSum(self, nums):
        nums.sort()
        i = 0
        j = 1
        k = 2
        ret = []
        while i < len(nums):
            while j < len(nums):
                while k < len(nums):
                    if k == len(nums)-1:
                        break
                    if nums[i] + nums[j] + nums[k] == 0:
                        ret.append([nums[i], nums[j], nums[k]])
                    while nums[k] == nums[k+1] and k < len(nums)-2:
                        k += 1
                    k += 1

                if j == len(nums)-2:
                    break
                while nums[j] == nums[j+1] and j < len(nums)-3:
                    j += 1
                j += 1
                k = j+1
            if i == len(nums)-3:
                break
            while nums[i] == nums[i+1] and i < len(nums)-4:
                i += 1
            i += 1
            j = i+1
            k = j+1
        return ret
