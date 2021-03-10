class Solution:
    def partition(self, s):
        ret = []
        memo = {}

        def helper(rest_str, weave):
            if not len(rest_str):
                ret.append(weave)
                return

            for i in range(1, len(rest_str)):
                new_weave = weave + [rest_str[:i]]
                if rest_str[:i] in memo:
                    helper(rest_str[i:], new_weave)

        helper(s, [])
        return ret

    def partition2(self, s):
        memo = {}

        def palindrome(s):
            return s == s[::-1]

        def helper(rest_str):
            memo[rest_str] = []
            if len(rest_str) == 1:
                memo[rest_str] = [[rest_str]]
                return

            for i in range(1, len(rest_str) + 1):
                this_time_str = rest_str[:i]
                taken_str = rest_str[i:]

                if palindrome(this_time_str):

                    if taken_str in memo:  # in memo
                        for l in memo[taken_str]:  # loop memo list value
                            memo[rest_str].append([this_time_str] + l)

                    else:
                        if taken_str != "":
                            helper(taken_str)
                            for l in memo[taken_str]:
                                memo[rest_str].append([this_time_str] + l)
                        else:
                            memo[rest_str].append([this_time_str])

        helper(s)
        return memo[s]
