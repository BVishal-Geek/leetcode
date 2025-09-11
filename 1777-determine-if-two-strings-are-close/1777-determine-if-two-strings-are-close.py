class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        list1 = sorted([word1.count(value) for value in set(word1)])
        list2 = sorted([word2.count(value) for value in set(word2)])

        if len(list1) != len(list2) or list1 != list2 or set(word1) != set(word2):
            return False
        else:
            return True