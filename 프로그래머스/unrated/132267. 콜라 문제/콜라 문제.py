def solution(a, b, n):
    answer = 0
    
    total = n
    while total >= a:
        answer += (total // a) * b
        total = (total % a) + (total // a) * b
    
    return answer