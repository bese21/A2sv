class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        strs = ""
        j = 0
        for i in range(len(s)):
            if j < len(spaces) and i == spaces[j]:
                strs += " "
                j+=1
            strs += s[i]
        return strs
