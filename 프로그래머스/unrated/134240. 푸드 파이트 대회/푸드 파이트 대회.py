def solution(food):
    left = ''.join([str(idx + 1) * (f//2) for idx, f in enumerate(food[1:])])
    return ''.join([left, '0', left[::-1]])