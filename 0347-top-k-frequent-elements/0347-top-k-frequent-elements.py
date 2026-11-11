import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        heap = []

        for n in nums:
            count[n] = count.get(n,0)+1

        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))

            if len(heap) > k: 
                heapq.heappop(heap)
        return [num for freq, num in heap] 



    