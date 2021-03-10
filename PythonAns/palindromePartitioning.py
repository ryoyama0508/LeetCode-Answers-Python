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


l = []
print([] + ["b", "c"])
l.append(["b", "c"])
print(l)