# 문제: 두 개 뽑아서 더하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    sums = set()

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            sums.add(numbers[i] + numbers[j])

    return sorted(sums)