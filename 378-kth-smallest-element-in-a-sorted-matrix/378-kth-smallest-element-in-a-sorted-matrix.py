import itertools
from heapq import heappush, heappop

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        nums = sorted(list(itertools.chain.from_iterable(matrix)))
        length = len(nums)
        return nums[k - 1]
        
        '''
        heap = []
        if k <= length / 2: #최소힙
            for num in nums:
                heappush(heap, (num, num))
        else: #최대힙
            for num in nums:
                heappush(heap, (-num, num))
            k = length - k + 1
            
        for _ in range(k - 1):
            heappop(heap)
            
        
        return heappop(heap)[1]
        '''
            
            
        