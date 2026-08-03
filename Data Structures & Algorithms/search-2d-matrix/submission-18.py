class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        length = rows * cols
        l = 0
        r = length - 1

        while l <= r:
            mid = (l + r) // 2
            row = (mid // cols)
            col = mid % cols
            print(f'l:{l}')
            print(f'r:{r}')
            print(f'row:{row}')
            print(f'col:{col}\n')
            midval = matrix[row][col]
            if midval < target:
                l = mid + 1
            elif midval > target:
                r = mid - 1
            else:
                return True
        return False