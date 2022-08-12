class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)

        while start <= end:
            speed = (start + end) // 2
            
            hour = 0
            for pile in piles:
                hour += ceil(pile / speed)
                
                if hour > h:
                    start = speed + 1
                    break    
            else:
                if hour <= h:
                    end = speed - 1
                  
        return end + 1
