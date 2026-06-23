# [성능 요약] 메모리: 12.3 MB 시간: 0.54 ms 

def solution(nums):
    s = set(nums)
    return min(len(nums)/2,len(s))