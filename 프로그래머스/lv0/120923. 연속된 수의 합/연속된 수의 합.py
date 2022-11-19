def solution(num, total):
    x = (total - sum([i for i in range(num)]))// num
    return [x + i for i in range(num)]