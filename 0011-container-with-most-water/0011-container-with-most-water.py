class Solution:
    def maxArea(self, height: List[int]) -> int:
        l_idx = 0
        r_idx = len(height) - 1
        
        _max = 0
        while l_idx != r_idx:
            _max = max(_max, (r_idx - l_idx) * min(height[l_idx], height[r_idx]))
            
            if height[l_idx] < height[r_idx]:
                l_idx += 1
            else:
                r_idx -= 1
            
        return _max