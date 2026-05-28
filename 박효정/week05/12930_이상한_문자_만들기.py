# 문제: 이상한 문자 만들기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    words = s.split(' ')
    answer = []
    for j in range(len(words)):
        new = ''
        for i in range(len(words[j])):
            if i % 2 == 0:
                new += words[j][i].upper()
            else:
                new += words[j][i].lower()
        answer.append(new)   
        
    return ' '.join(answer)