class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge case
        if len(s) != len(t):
            return False
        
        if sorted(s) != sorted(t):
            return False
        return True