class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        maxCandies = max(candies)
        boolList = []
        initialKid = 0
        statement = False
        while initialKid < len(candies):
            if candies[initialKid] + extraCandies >= maxCandies: 
                boolList.append(not statement)
            else:
                 boolList.append(statement)

            initialKid += 1
        return boolList
       