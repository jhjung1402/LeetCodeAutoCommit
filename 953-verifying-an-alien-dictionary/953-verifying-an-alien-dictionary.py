class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        human_order = 'abcdefghijklmnopqrstuvwxyz'
        alien_order = {}
        for i, v in enumerate(order):
            alien_order[v] = human_order[i]
        
        answer = False
        pre_str2int = ''
        for word in words:
            str2int = ''
            for w in word:
                str2int += alien_order[w]
            if pre_str2int <= str2int:
                pre_str2int = str2int
            else:
                break
        else:
            answer = True
            
        return answer