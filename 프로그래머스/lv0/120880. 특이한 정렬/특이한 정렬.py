def solution(numlist, n):
    return sorted(numlist, key = lambda x : (abs(x - n), -x))
                  
    '''
    answer = [(abs(num - n), num) for num in numlist]
    answer = sorted(answer, key = lambda x : (x[0], -x[1]))
    return  [x[1] for x in answer]
    '''