from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        groups = defaultdict(list)
        for s in strs:
            groups[tuple(sorted(s))].append(s)
        return groups.values()
