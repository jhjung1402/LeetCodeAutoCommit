class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        locations = [0] * 1000
        for np, f, t in trips:
            for idx in range(f, t):
                locations[idx] += np
                if capacity < locations[idx]:
                    return False
        return True
                    