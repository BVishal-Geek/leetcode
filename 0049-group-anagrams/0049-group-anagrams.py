class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()

        for keys in strs:
            word = ''.join(sorted(keys))
            if word not in hashmap:
                hashmap[word] = []
            hashmap[word].append(keys)
        return list(hashmap.values())
        