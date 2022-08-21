class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = -prices[0]
        sell = 0
        
        for i in range(len(prices)):
            _buy = buy
            _sell = sell
            
            buy = max(buy, _sell - prices[i])
            sell = max(sell, _buy + prices[i] - fee)
        
        return max(buy, sell)
        
        
        '''     
        def recursive(bs, start, profit):
            if start == len(prices):
                return profit 

            _max = 0
            for idx in range(start, len(prices)):
                if not bs:
                    _max = max(_max, recursive([], idx + 1, profit)) # 안 산 경우
                    _max = max(_max, recursive([prices[idx]], idx + 1, profit)) # 산 경우

                elif prices[idx] - bs[0] - fee > 0:
                    _max = max(_max, recursive(bs, idx + 1, profit)) # 안 판 경우
                    _max = max(_max, recursive([], idx + 1, profit + prices[idx] - bs[0] - fee)) # 판 경우

            return _max

        _max = 0
        for idx in range(len(prices)):
            _max = max(_max, recursive([], idx + 1, 0)) # 안 산 경우
            _max = max(_max, recursive([prices[idx]], idx + 1, 0)) # 산 경우

        return _max
        '''