# 문제: JadenCase 문자열 만들기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = ''
    isFirst = True
    for l in s:
        if l == ' ':
            isFirst = True
            answer += ' '
            continue
        if isFirst:
            answer += l.upper()
            isFirst = False
        else:
            answer += l.lower()

    return answer


def Jaden_Case(s):
    answer =[]
    for i in range(len(s.split())):
        answer.append(s.split()[i][0].upper() + s.split()[i].lower()[1:])
    return " ".join(answer)