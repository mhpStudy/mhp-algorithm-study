# 문제: 숫자 문자열과 영단어
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    idx = 0
    answer = ''
    while idx < len(s):
        if s[idx].isdigit():
            answer += s[idx]
            idx += 1
        elif s[idx] == 'z':
            answer += '0'
            idx += 4
        elif s[idx] == 'o':
            answer += '1'
            idx += 3
        elif s[idx] == 't':
            if s[idx + 1] == 'w':
                answer += '2'
                idx += 3
            else:
                answer += '3'
                idx += 5
        elif s[idx] == 'f':
            if s[idx + 1] == 'i':
                answer += '5'
                idx += 4
            else:
                answer += '4'
                idx += 4
        elif s[idx] == 's':
            if s[idx + 1] == 'i':
                answer += '6'
                idx += 3
            else:
                answer += '7'
                idx += 5
        elif s[idx] == 'e':
            answer += '8'
            idx += 5
        else:
            answer += '9'
            idx += 4

    return int(answer)




# num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
#
# def solution(s):
#     answer = s
#     for key, value in num_dic.items():
#         answer = answer.replace(key, value)
#     return int(answer)