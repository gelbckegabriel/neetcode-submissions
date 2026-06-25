class Solution:
    def isAnagram(self, s: str, t: str) -> bool:        
        s = list(s)
        t = list(t)
        sDict, tDict = {}, {}

        if len(s) != len(t):
            return False

        for index, char in enumerate(s):
            if sDict.get(char) is None:
                sDict[char] = 1
            else:
                sDict[char] = sDict.get(char) + 1

            if tDict.get(t[index]) is None:
                tDict[t[index]] = 1
            else:
                tDict[t[index]] = tDict.get(t[index]) + 1
        
        for key, value in sDict.items():
            if tDict.get(key) != value or tDict.get(key) is None:
                return False
        
        return True