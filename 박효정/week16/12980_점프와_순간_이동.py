# 문제: 점프와 순간 이동
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12980
 # [성능 요약] 메모리: 11.2 MB 시간: 0.01 ms    

'''
뒤에서부터 센다
짝수일땐 순간이동
홀수일땐 점프
'''
def solution(n):
    ans = 1
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n -= 1
            ans += 1
    return ans
