# 문제: 멀리 뛰기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12914

def solution(n):
    '''
    DP 문제라는 느낌이 든다.
    1 - 1
    2 - 2
    3 - 3
    4 - 5. 1로 시작한 경우 남은게 3, 2로 시작한 경우 남은게 2이므로 2+3
    5 - 1로 시작한 경우 남은게 4, 2로 시작한 경우 남은게 3
    피보나치 수열이네?
    '''
    if n == 1: return 1
    if n == 2: return 2
    answer = 0
    prev1, prev2 = 2, 1
    for _ in range(3,n+1):
        answer = prev1 + prev2
        prev1, prev2 = answer, prev1
    return answer%1234567   # n<=2000이면 마지막에만 나누어도 될 듯


'''
def solution(n):
    a, b = 1, 2

    if n == 1:
        return 1

    for _ in range(3, n + 1):
        a, b = b, (a + b) % 1234567

    return b
'''
