class Solution:
    def maxProduct(self, words: List[str]) -> int:
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
                
                
        
        