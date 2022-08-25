class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        _max, _min, answer = nums[0], nums[0], nums[0]
        
        for i in range(1, len(nums)):
            __max = max(nums[i], _max * nums[i], _min * nums[i])
            __min = min(nums[i], _max * nums[i], _min * nums[i])
            _max, _min = __max, __min
            answer = max(answer, _max)
        
        return answer
            