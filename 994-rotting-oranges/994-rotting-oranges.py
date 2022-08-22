class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        fresh = 0
        dq = deque()
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    dq.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
                    
        minute = -1
        while dq:
            minute += 1
            length = len(dq)
            for _ in range(length):
                r, c = dq.popleft()
                for dr, dc in dirs:
                    if (0 <= r + dr) and (r + dr < R) and (0 <= c + dc) and (c + dc < C) and (grid[r + dr][c + dc] == 1):
                        grid[r + dr][c + dc] = 2
                        dq.append((r + dr, c + dc))
                        fresh -= 1
        else:
            if fresh != 0:
                return -1
            
        return 0 if minute < 0 else minute
        