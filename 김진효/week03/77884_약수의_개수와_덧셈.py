 # [성능 요약] 메모리: 9.16 MB 시간: 1.11 ms 

def solution(left, right):
    answer = 0
    for num in range(left,right+1):
        num_sqrt = num**0.5
        # 소수점이 있는 경우 -> 제곱근 x
        if  num_sqrt - int(num_sqrt) > 0:
            answer += num
        # 소수점이 없는 경우 -> 제곱근 o
        else:
            answer -= num        
            
    return answer