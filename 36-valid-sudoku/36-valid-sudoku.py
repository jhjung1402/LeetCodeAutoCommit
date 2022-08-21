class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        
        for row in board:
            nums = []
            
            for i in row:
                if i in nums:
                    return False
                elif i != '.':
                    nums.append(i)
        
        for i in range(N):
            nums = []
            for row in board: 
                if row[i] in nums:
                    return False
                elif row[i] != '.':
                    nums.append(row[i])
                    
        for i in range(0, N, 3):
            for j in range(0, N, 3):
                nums = []
                for _i in range(i, i + 3):
                    for _j in range(j, j + 3):
                        if board[_i][_j] in nums:
                            return False
                        elif board[_i][_j] != '.':
                            nums.append(board[_i][_j])
                        
        return True