# 문제: 시저 암호
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    answer = ""

    for ch in s:
        if ch == " ":
            answer += " "

        elif ch.isupper():
            answer += chr((ord(ch) - ord('A') + n) % 26 + ord('A'))

        else:
            answer += chr((ord(ch) - ord('a') + n) % 26 + ord('a'))

    return answer