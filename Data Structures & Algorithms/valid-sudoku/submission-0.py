class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset = defaultdict(set)
        colset = defaultdict(set)
        boxset = defaultdict(set)

        ''' rowset : {
            0 : set(1 2 3 4 5 6 7 8 9)
            1 : set(1 2 3 4 5 6 7 8 9)
        } where key is row and val is set of values
        '''
        ''' colset : {
            0 : set(1 2 3 4 5 6 7 8 9)
            1 : set(1 2 3 4 5 6 7 8 9)
        } where key is col and val is set of values
        '''
        ''' boxset : {
            (0,0) : set(1 2 3 4 5 6 7 8 9)
            (0,1) : set(1 2 3 4 5 6 7 8 9)
            (0,2) : set(1 2 3 4 5 6 7 8 9)
        } where key is tuple and val is set of values
        '''

        # iterates each row
        # [ 1 2 3 4 5 6 7 8 9] -> 
        # [ 1 2 3 4 5 6 7 8 9] ...
        for row in range(9):
            # [ . ] -> [ 2 ] -> [ 3 ] ...
            # iterates each box in row
            for col in range(9):
                if board[row][col] == ".":
                    continue
                
                if (
                    board[row][col] in rowset[row] or
                    board[row][col] in colset[col] or
                    board[row][col] in boxset[(row // 3, col // 3)]
                ):
                    return False
                
                rowset[row].add(board[row][col])
                colset[col].add(board[row][col])
                boxset[(row // 3, col // 3)].add(board[row][col])
        return True
                    

                


