class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        diag = defaultdict(set)
        for i in range(9): #rows
            for j in range(9): #cols
                if board[i][j] == '.':
                    continue
                if (board[i][j] in rows[i] or 
                   board[i][j] in cols[j] or
                   board[i][j] in diag[(i // 3, j // 3)]):
                   return False
                cols[j].add(board[i][j])
                rows[i].add(board[i][j])
                diag[(i // 3, j // 3)].add(board[i][j])
        return True
                
                
               

      
      


        
        