class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        uniqueOccuranceList = []
        Dictionary = {key:arr.count(key) for key in set(arr)}
        for i in set(arr): 
            if Dictionary[i] in uniqueOccuranceList:
                return False   
            else:
                uniqueOccuranceList.append(Dictionary[i])
        return True 