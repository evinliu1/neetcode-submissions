class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minB = r

        def _get_hours(bananas):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/bananas)
            print(f"bananas: {bananas} hours: {hours}")
            return hours

        while l <= r:
            mid = (l + r) // 2
            hours = _get_hours(mid)
            if hours <= h:
                minB = mid
                r = mid - 1
            else:
                l = mid + 1
        return minB
        
