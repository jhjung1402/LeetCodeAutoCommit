class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words = list(set(words))   
    
        _max = 0
        for i in range(0, len(words)):
            w1 = words[i]
            for j in range(i + 1, len(words)):
                w2 = words[j]

                if _max < len(w1) * len(w2) and not (set(w1) & set(w2)):
                    _max = max(_max, len(w1) * len(w2))
        return _max
        
                
        
        