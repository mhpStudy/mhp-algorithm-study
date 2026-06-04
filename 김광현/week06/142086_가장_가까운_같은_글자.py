# 문제: 가장 가까운 같은 글자
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/142086

def solution(s):
    answer = []
    last_index = {}
    
    for i in range(len(s)):
        character = s[i]
        
        if character in last_index:
            answer.append(i-last_index[character])
        else:
            answer.append(-1)
            
        last_index[character] = i
    
    return answer