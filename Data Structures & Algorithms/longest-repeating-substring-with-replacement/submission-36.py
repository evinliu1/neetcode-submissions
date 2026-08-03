class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charset = set(s)
        #(A,B)

        res = 0

        for char in charset:
            count = 0
            l = r = 0
            print(f'char: {char}')
            while r < len(s):
                if s[r] != char:
                    count += 1
                while count > k:
                    if s[l] != char:
                        count -= 1
                    l += 1
                res = max(res, r - l + 1)
                print(f'result: {res}')
                print(f'char: {s[r]}')
                print(f'r: {r}')
                print(f'count: {count} k: {k}')
                r += 1
        return res

                