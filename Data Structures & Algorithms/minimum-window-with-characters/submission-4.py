class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        '''
        {
            X: 1
            Y: 1
            Z: 1
        }
        '''
        res, resLen = [-1, -1], float("inf")
        ct, curr = {}, {}
        for c in t:
            ct[c] = ct.get(c, 0) + 1
        have, needs = 0, len(ct)
        l = 0

        for r in range(len(s)):
            c = s[r]
            curr[c] = curr.get(c, 0) + 1

            if c in ct and ct[c] == curr[c]:
                have += 1
                
            while have == needs:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                curr[s[l]] -= 1
                if s[l] in ct and curr[s[l]] < ct[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("inf") else ""