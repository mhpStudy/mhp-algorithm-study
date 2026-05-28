# 문제: 숫자의 표현
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    answer = 1 # 본인 포함 
    
    # 1~ n//2까지 돌리면서 , 내부에서 다시 다음 수 ~ n//2 + 1까지 돌림
    for i in range(1, n//2+1):
        s_num = i
        for j in range(i+1, n//2+2):
            s_num += j
            
            if s_num == n:
                answer += 1
                break
                
            if s_num > n:
                break
    
    return answer