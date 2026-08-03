class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        lowered = s.lower().replace(" ", "")
        l = 0
        r = len(lowered) - 1

        print(lowered)

        while l <= r:
            while not lowered[l].isalnum() and l < r:
                l += 1
            while not lowered[r].isalnum() and l < r:
                r -= 1
            print(f"l: {l} r: {r}\nl: {lowered[l]} r: {lowered[r]}")
            if lowered[l] != lowered[r]:
                return False
            l += 1
            r -= 1
        return True