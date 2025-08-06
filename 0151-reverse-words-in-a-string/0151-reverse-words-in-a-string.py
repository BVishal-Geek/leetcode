class Solution:
    def reverseWords(self, s: str) -> str:
        wordStorage = s.strip().split()
        return ' '.join(wordStorage[::-1])