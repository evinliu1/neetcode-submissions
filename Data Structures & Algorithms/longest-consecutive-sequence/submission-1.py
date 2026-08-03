class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
#       2 20 4 10 3 4 5
#                   ^
        '''
            {
                2 : 4
            20 : 1
                4 : 3
            10 : 1
                3 : 3
                5 : 4
            
            }

            res = 3
        '''
        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
                res = max(res, mp[num])
        return res
        