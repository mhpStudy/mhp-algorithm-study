 # [성능 요약] 메모리: 9.27 MB 시간: 0.01 ms 

def solution(s):
    answer = True
    
    if not s.isdigit():
        return False
    
    if len(s) != 4 and len(s) != 6:
        return False
     
    return answer