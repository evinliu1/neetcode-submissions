class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        flattened = [item for sublist in matrix for item in sublist]
        l, r = 0, len(flattened) - 1
        while l <= r:
            mid = (l + r) // 2
            if flattened[mid] > target:
                r = mid - 1
            elif flattened[mid] < target:
                l = mid + 1
            else:
                return True
        
        return False