class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        '''
        Explanation: 
            We have a string from which we need to partition them
            in a way the each character should be only in one group. 
            It can be repeated in the same group but it should not be
            in the other group. 
            We need to return a list where the list contains the length of
            each string length. 

        Logic:
            We are checking the last occurance of each character. 
            if the current character last occurance is greater than 
            the last occurance of last character we will change the value. 
            if the last occurance and the index of the current character equals same,
            we get 1st partition of string. 
        '''
        lastIndex = {}

        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        size, end = 0,0
        for i, c in enumerate(s):
            size +=1
            end = max(end, lastIndex[c])
            if i == end:
                res.append(size)
                size = 0
        return res