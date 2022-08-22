class Solution:
    def maxProduct(self, words: List[str]) -> int:
        '''
        dic = {}
        
        for word in words:
            alpha_list = set(word) # 알파벳 중복 제거
            dic.update({word:alpha_list})

        _max = 0
        key_list = list(dic.keys())
        for k1 in key_list[:-1]:
            for k2 in key_list[1:]:
                if not (dic[k1] & dic[k2]): # 두 알파벳집합의 교집합이 없는 경우
                    _max = max(_max, len(k1) * len(k2))
        
        return _max
        '''
        _max = 0
        for i in range(0, len(words)):
            w1 = words[i]
            al1 = set(w1)
            for j in range(i + 1, len(words)):
                w2 = words[j]
                al2 = set(w2)
                
                if not (al1 & al2):
                    _max = max(_max, len(w1) * len(w2))
        return _max
        
                
        
        