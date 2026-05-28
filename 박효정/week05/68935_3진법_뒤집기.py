# 문제: 3진법 뒤집기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    # 3진법 변환
    # n // 3을 계속 //3하고 (3보다 작아질 때 까지), 나머지를 뒤에서부터 붙인다
    num_3 = ''
    while n >0:
        num_3 += str(n % 3)
        n = n // 3
    
    # 10진법 변환
    # 뒤에서부터 3**0 * n
    num_10 = num_3[::-1]
    answer = 0
    
    for i in range(len(num_10)):
        answer += 3**i * int(num_10[i])    

    return answer