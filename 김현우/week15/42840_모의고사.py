# 문제: 모의고사
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    score = [0, 0, 0]
    length = len(answers)
    one = [1, 2, 3, 4, 5] * (len(answers) // 5 + 1)
    two = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers) // 8 + 1)
    thr = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers) // 10 + 1)

    for i in range(length):
        if answers[i] == one[i]: score[0] += 1
        if answers[i] == two[i]: score[1] += 1
        if answers[i] == thr[i]: score[2] += 1

    for i in range(3):
        if score[i] == max(score): answer.append(i + 1)

    return answer
