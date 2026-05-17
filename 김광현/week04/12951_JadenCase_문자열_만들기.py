# 문제: JadenCase 문자열 만들기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    words = s.split(" ")
    result = []
    for word in words:
        if word == "":
            result.append("")
        else:
            result.append(word[0].upper() + word[1:].lower())
    return " ".join(result)