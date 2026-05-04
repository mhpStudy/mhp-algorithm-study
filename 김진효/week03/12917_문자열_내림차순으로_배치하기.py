 # [성능 요약] 메모리: 9.23 MB 시간: 0.06 ms 

def solution(s):
    answer = []
    
    arr = list(map(ord, s))
    arr.sort(reverse=True)
    
    answer = ''.join(map(chr,arr))
    
    return answer