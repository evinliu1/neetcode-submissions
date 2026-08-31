class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2 # first attribute each list to A and B
        total = len(nums1) + len(nums2) # find the total length of A + B
        half = total // 2 # find the half length of the total length so ( A + B ) // 2

        if len(B) < len(A): # We want to make sure that the shorter one is A for our purposes
            A, B = B, A
        
        l, r = 0, len(A) - 1 # left and right pointers. we'll find the medium of the shorter list first

        while True:
            i = (l + r) // 2 # middle index for A
            j = half - i - 2 # B takes the remaining - 2 for 0 indexes

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")
 
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return (min(Aright, Bright))
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1