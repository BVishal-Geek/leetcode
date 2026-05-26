class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        FreqElements = dict()

        for elements in nums: 
            if elements not in FreqElements: 
                FreqElements[elements] = 1 
            else: 
                FreqElements[elements]+=1 
        sort = sorted(FreqElements.items(), key = lambda x:x[1], reverse=True)
        return [tuple[0] for tuple in sort[:k]]