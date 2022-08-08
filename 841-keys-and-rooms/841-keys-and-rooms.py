class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        unlock = [False] * len(rooms)
        
        
        dq = deque()
        dq.append(0)
        
        while dq:
            idx = dq.popleft()
            unlock[idx] = True
            
            for room in rooms[idx]:
                if not unlock[room]:
                    dq.append(room)
            
        return False if unlock.count(False) > 0 else True
            
            
            