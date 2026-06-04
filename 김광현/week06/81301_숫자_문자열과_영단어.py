# 문제: 숫자 문자열과 영단어
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    words = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    answer = ""
    temp = ""

    for ch in s:
        if ch.isdigit():
            answer += ch
        else:
            temp += ch

            if temp in words:
                answer += words[temp]
                temp = ""

    return int(answer)