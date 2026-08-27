# 문제: 사칙연산
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/1843

def solution(arr):
    groups = ''.join(arr).split('-')

    first = sum(map(int, groups[0].split('+')))

    if len(groups) == 1:
        return first

    right_min = 0
    right_max = 0

    for group in groups[:0:-1]:
        nums = list(map(int, group.split('+')))

        group_min = -sum(nums)
        group_max = sum(nums[1:]) - nums[0]

        next_min = min(
            group_min + right_min,
            group_min - right_max
        )

        next_max = max(
            group_max + right_max,
            group_min - right_min
        )

        right_min, right_max = next_min, next_max

    return first + right_max


'''
def solution(arr):
    nums = list(map(int, arr[::2]))
    ops = arr[1::2]

    n = len(nums)

    dp_max = [[float('-inf')] * n for _ in range(n)]
    dp_min = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        dp_max[i][i] = nums[i]
        dp_min[i][i] = nums[i]

    # length = 구간에 포함된 숫자 개수
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            for k in range(i, j):
                if ops[k] == '+':
                    max_value = dp_max[i][k] + dp_max[k + 1][j]
                    min_value = dp_min[i][k] + dp_min[k + 1][j]

                else:
                    max_value = dp_max[i][k] - dp_min[k + 1][j]
                    min_value = dp_min[i][k] - dp_max[k + 1][j]

                dp_max[i][j] = max(dp_max[i][j], max_value)
                dp_min[i][j] = min(dp_min[i][j], min_value)

    return dp_max[0][n - 1]
'''
