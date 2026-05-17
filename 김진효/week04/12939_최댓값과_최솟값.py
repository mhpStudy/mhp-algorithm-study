 # [성능 요약] 메모리: 9.36 MB 시간: 0.06 ms 

def solution(s):
    sl = list(s.split())
    max_v = int(sl[0])
    min_v = int(sl[0])
    
    for i in range(1, len(sl)):
        v = int(sl[i])
        max_v = max(max_v, v)
        min_v = min(min_v, v)
        
    return f"{min_v} {max_v}"