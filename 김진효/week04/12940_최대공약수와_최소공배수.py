'''
[최대 공약수]
유클리드 호제법
-> a와 b의 최대공약수는 b와 a를 b로 나눈 나머지의 최대공약수와 같다
이 성질에 따라 a를 b로 나눈 나머지가 0이 될 때까지 반복하여 최대공약수를 구함

a   b   a%b
72  30  12
30  12  6
12  6   0 

최대 공약수: 6

[최소공배수]
최소공배수 = (a*b) / 최대공약수

 # [성능 요약] 메모리: 9.12 MB 시간: 0.00 ms 
'''

def solution(n, m):
    answer = []

    # 최대 공약수 GCD
    a, b = n, m
    while b > 0:
        a, b = b, a % b

    answer.append(a)

    # 최소 공배수 LCD
    answer.append(n*m//a)

    return answer


'''
위 모른다고 치고 순정으로 가면
# [성능 요약] 메모리: 9.03 MB 시간: 0.15 ms 
'''

def solution2(n, m):
    answer = []

    gcd = 0
    # 최대 공약수
    for i in range(1, m+1):
        if n%i == 0 and m%i == 0:
            gcd = max(gcd,i)

    answer.append(gcd)

    # 최소 공배수
    lcd = gcd * (n//gcd) * (m//gcd)

    answer.append(lcd)

    return answer


'''
math의 lcm 함수는 python 3.9 이상 에서만 지원
 # [성능 요약] 메모리: 9.15 MB 시간: 0.00 ms 
'''
import math
def solution3(n, m):
    answer = []

    answer.append(math.gcd(n,m))
    # answer.append(math.lcm(n,m))

    # 최소 공배수 LCD   
    answer.append(n*m//answer[0])

    return answer

print(solution(3,12))