# 문제: 숫자 문자열과 영단어
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    answer = ''
    alpha = {'zero' : '0',
             'one' : '1',
             'two' : '2',
             'three' : '3',
             'four' : '4',
             'five' : '5',
             'six' : '6',
             'seven' : '7',
             'eight' : '8',
             'nine' : '9'
            }
           
    idx = 0
    while idx < len(s):
        if s[idx].isdigit():
            answer += str(s[idx])
            idx += 1
            continue
        else:
            a = ''
            while idx < len(s) and not s[idx].isdigit():
                a += s[idx]
                if a in alpha:
                    answer += alpha[a]
                    idx += 1
                    break
                idx += 1

    '''
    for word, num in alpha.items():
        s = s.replace(word, num)
    '''
    
    return int(answer)