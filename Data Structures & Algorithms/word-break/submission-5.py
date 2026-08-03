class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def df(remaining):
            if not remaining:
                return True
            if remaining in memo:
                return memo[remaining]
            for i in range(len(remaining) + 1):
                if remaining[0:i] in wordDict and df(remaining[i:]):
                    memo[remaining] = True
                    return True
            memo[remaining] = False
            return False

        return df(s)