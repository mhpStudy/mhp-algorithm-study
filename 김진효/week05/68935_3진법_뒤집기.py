 # [성능 요약] 메모리: 9.17 MB 시간: 0.03 ms 

def solution(n):
    # 3진법
    t = ''
    while n > 0:
        t += str(n % 3)
        n //= 3

    # 10진법
    # return int(t,3)
    
    t = str(int(t))
    tl = len(t)
    d = 0 
    for idx in range(tl):
        d += int(t[tl- 1 - idx]) * (3**idx)

    return d

print(solution(45))
