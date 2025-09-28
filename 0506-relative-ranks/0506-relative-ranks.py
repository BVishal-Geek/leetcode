import heapq

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = []

        for i, scores in enumerate(score):
            heapq.heappush(heap, (-scores,i))
        
        result = [""] * len(score)
        ranks = ['Gold Medal', 'Silver Medal', 'Bronze Medal']

        rank = 1
        while heap: 
            neg_score, i = heapq.heappop(heap)
            if rank <= 3: 
                result[i] = ranks[rank-1]
            else: 
                result[i] = str(rank)
            rank += 1 
        return result