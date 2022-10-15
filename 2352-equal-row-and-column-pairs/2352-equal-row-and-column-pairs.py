class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows = grid
        
        cols = list(map(list, zip(*grid)))
      
        cnt = 0
        for row in rows:
            for col in cols:
                if row == col:
                    cnt += 1
        return cnt