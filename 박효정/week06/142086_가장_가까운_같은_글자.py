# 문제: 가장 가까운 같은 글자
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/142086

def solution(s):
    answer = []
    # 딕셔너리에 문자 : 인덱스 를 저장하자.
    last_idx = {}
    for i in range(len(s)):
        ch = s[i]
        # 앞에서 나온 문자라면
        if ch in last_idx: 
            answer.append(i-last_idx[ch])
        # 나온 적 없는 문자라면
        else:
            answer.append(-1)
        last_idx[ch] = i
            
    return answer
