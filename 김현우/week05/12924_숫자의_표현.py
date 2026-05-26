# 문제: 숫자의 표현
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12924

# 성능 요약
# 메모리: 9.15 MB
# 시간: 1.17 ms
def solution(n):
    answer, start, end, interval_sum = 0, 1, 1, 0
    while start <= n:
        if interval_sum < n:
            interval_sum += end
            end += 1
        else:
            if interval_sum == n:
                answer += 1
            interval_sum -= start
            start += 1

    return answer

# 성능 요약
# 메모리: 9.27 MB
# 시간: 3.40 ms
# def solution(n):
#     answer = 0
#     for start in range(1, n + 1):
#         interval_sum = 0
#         end = start
#         while interval_sum < n:
#             interval_sum += end
#             end += 1
#         if interval_sum == n: answer += 1
#
#     return answer

# 성능 요약
# 메모리: 9.14 MB
# 시간: 0.02 ms
# def solution(n):
#     answer = 1  # 1개의 자연수로 표현 가능
#     nn = n*2
#
#     # i개의 자연수로 표현 가능한지 확인할 것
#     # i의 이론상 최댓값은? 1부터i의합이 n을 초과하면 불가능함
#     # 따라서, int((2*n)**(1/2))
#     maxi = int((2*n)**(1/2))
#     print(maxi)
#
#     # i가 홀수인 경우
#     # i로 나누어떨어져야하고, 1부터i의합 = 1+i//2*i 이상이어야 함
#     for i in range(3,maxi+1,2):
#         if n%i==0 and 1+i//2*i <= n: answer += 1
#
#     # i가 짝수인 경우
#     # n*2가 i로 나누어떨어져야하고, n은 i로 나누어떨어지지않고, (1+i)*i 이상이어야 함
#     for i in range(2,maxi+1,2):
#         if nn%i==0 and n%i!=0 and (1+i)*i <= nn: answer += 1
#
#     return answer

# 성능 요약
# 메모리: 9.07 MB
# 시간: 0.16 ms
# def solution(num):
#     return len([i  for i in range(1,num+1,2) if num % i is 0])