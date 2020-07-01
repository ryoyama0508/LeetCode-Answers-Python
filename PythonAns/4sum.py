class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        i = 0
        j = 1
        l = 2
        r = len(nums)-1
        ret = []
        while i < len(nums)-3:
            while j < len(nums)-2:
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        ret.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1

                while j < len(nums)-2 and nums[j] == nums[j+1]:
                    j += 1
                j += 1
                l = j+1
                r = len(nums)-1

            while i < len(nums)-3 and nums[i] == nums[i+1]:
                i += 1
            i += 1
            j = i+1
            l = j+1
            r = len(nums)-1

        return ret
