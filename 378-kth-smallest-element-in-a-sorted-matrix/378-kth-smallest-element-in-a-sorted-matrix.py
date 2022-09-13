import itertools
from heapq import heappush, heappop

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        nums = sorted(list(itertools.chain.from_iterable(matrix))) #2차원 배열을 1차원으로 변환
        return nums[k - 1]
            
            
        