# 문제: JadenCase 문자열 만들기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    arr = s.split(' ')
    new_arr = []
    
    for w in arr:
        if w == '':
            new_arr.append('')
        
        else:
            new_w = w[0].upper() + w[1:].lower()
            new_arr.append(new_w)
    
    return ' '.join(new_arr)