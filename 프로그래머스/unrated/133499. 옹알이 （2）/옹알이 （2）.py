def solution(babblings):
    answer = 0
    
    words = ["aya", "ye", "woo", "ma"]
    
    for babbling in babblings:
        li = []

        while len(babbling) != 0:
            if (len(babbling) >= 3 and babbling[0:3] == 'aya') and (len(li) == 0 or li[-1] != 'aya'):
                li.append('aya')
                babbling = babbling[3:]

            elif (len(babbling) >= 2 and babbling[0:2] == 'ye')  and (len(li) == 0 or li[-1] != 'ye'):
                li.append('ye')
                babbling = babbling[2:]

            elif (len(babbling) >= 3 and babbling[0:3] == 'woo')  and (len(li) == 0 or li[-1] != 'woo'):
                li.append('woo')
                babbling = babbling[3:]

            elif (len(babbling) >= 2 and babbling[0:2] == 'ma')  and (len(li) == 0 or li[-1] != 'ma'):
                li.append('ma')
                babbling = babbling[2:]

            else:
                break

        answer += 1 if len(babbling) == 0 else 0
            
    return answer