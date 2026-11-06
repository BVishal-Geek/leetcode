from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for elements in strs: 
            sorted_elements = sorted(elements)
            key = ''.join(sorted_elements)
            groups[key].append(elements)
        return list(groups.values())
        