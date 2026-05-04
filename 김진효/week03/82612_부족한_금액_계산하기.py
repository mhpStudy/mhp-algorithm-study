 # [성능 요약] 메모리: 9.08 MB 시간: 0.11 ms 

def solution(price, money, count):
    s = 0
    
    for p in range(price, price*count+1, price):
        s += p
    
    return 0 if s <= money else s - money