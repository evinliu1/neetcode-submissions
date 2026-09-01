class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(nums2) < len(nums1):
            A, B = B, A
        
        total = len(A) + len(B)
        half = total // 2
        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2

            ALEFT = A[i] if i >= 0 else float("-inf")
            BLEFT = B[j] if j >= 0 else float("-inf")
            ARIGHT = A[i + 1] if (i + 1) < len(A) else float("inf")
            BRIGHT = B[j + 1] if (j + 1) < len(B) else float("inf")

            if ALEFT <= BRIGHT and BLEFT <= ARIGHT:
                if total % 2: # then we know it's an odd length
                    return min(ARIGHT, BRIGHT)
                else:
                    return (max(ALEFT, BLEFT) + min(ARIGHT, BRIGHT)) / 2
            elif ALEFT > BRIGHT:
                r = i - 1
            else:
                l = i + 1