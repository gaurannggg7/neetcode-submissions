class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        isAnagram = sorted(s) == sorted(t)
        return isAnagram