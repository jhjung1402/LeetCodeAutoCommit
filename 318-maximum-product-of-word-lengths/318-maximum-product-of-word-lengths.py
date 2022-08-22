class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words = list(set(words)) # 단어 중복 제거
        
        _max = 0
        for i in range(0, len(words)):
            w1 = words[i]
            for j in range(i + 1, len(words)):
                w2 = words[j]

                if not (set(w1) & set(w2)): # 두 단어의 알파벳 교집합이 없는 경우
                    _max = max(_max, len(w1) * len(w2))
        return _max
        
                
        
        