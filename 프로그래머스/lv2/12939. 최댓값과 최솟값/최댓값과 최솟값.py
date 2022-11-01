def solution(s):
    nums = list(map(int, s.split(" ")))
    return '{0} {1}'.format(min(nums), max(nums))