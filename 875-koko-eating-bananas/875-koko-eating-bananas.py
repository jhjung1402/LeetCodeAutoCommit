class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)

        
        while start <= end:
            speed = (start + end) // 2
            
            hour = sum([ceil(pile / speed) for pile in piles])
                 
            if hour <= h:
                end = speed - 1
            else:
                start = speed + 1

        return end + 1
