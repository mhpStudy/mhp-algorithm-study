# - 별로 묶고 구간 별로 최소/최대 구하기
# 맨 첫 연산이 - 일때는 부호가 바뀌면서 최대값일 가능성이 있기 때문
# **알고리즘: 연속행렬곱셈 응용 [DP 문제]


def solution(arr):
    answer = -1
    return answer


# 뒤 부터 보면서 괄호 씌울지 말지 고민..? -> - 값들이 더해지면서 최대가 될 수 있음
# def solution(arr):
#     answer = 0

#     if arr[-2] == "+":
#         answer += int(arr[-1])
#     elif arr[-2] == "-":
#         answer -= int(arr[-1])

#     for i in range(len(arr)-3,-1,-1):
#         if i == 0 and arr[i].isdecimal():
#             answer += int(arr[i])

#         if arr[i] == '+':
#             answer += int(arr[i+1])

#         elif arr[i] == '-':
#             answer = max(answer - int(arr[i+1]), -(answer + int(arr[i+1])))

#     return answer

# print(solution(["1", "-", "3", "+", "5", "-", "8"]))
# print(solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"]))
print(solution(["1", "-", "2", "-", "3", "-", "4"]))