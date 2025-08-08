class Solution:
    def compress(self, chars: List[str]) -> int:
        initialCharacter = chars[0]
        characterCount = 1
        compressedList = []
        if len(chars) == 1:
            return 1

        for index in range(1, len(chars)):
            if chars[index] == initialCharacter:
                characterCount += 1
            else:
                compressedList.append(initialCharacter)
                if characterCount > 1:
                    compressedList.extend(str(characterCount))
                initialCharacter = chars[index]
                characterCount = 1

        # handle the final run
        compressedList.append(initialCharacter)
        if characterCount > 1:
            compressedList.extend(str(characterCount))

        # write back
        for i in range(len(compressedList)):
            chars[i] = compressedList[i]

        return len(compressedList)
