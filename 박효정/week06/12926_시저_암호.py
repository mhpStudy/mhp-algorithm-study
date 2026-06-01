# 문제: 시저 암호
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    answer = ''

    # 91 ~ 96 / 123~ 라면 -26
#     for i in s:
#         o = ord(i)
        
#         if 65 <= o <= 90 and 91 <= o + n:
#             answer += chr(o + n - 26)
#         elif 97 <= o and o + n > 122:
#             answer += chr(o + n - 26)
#         elif o == 32:
#             answer += ' '
#         else:
#             answer += chr(o + n)

    for ch in s:
        if ch == ' ':
            answer += ' '
        elif 'A' <= ch <= 'Z':
            # 1. ord(ch) - ord('A') : A를 기준으로 0부터 세기
            #   A : 0 , B : 1, C : 2
            # 2. + n : n 칸 이동
            # 3. % 26 : Z를 넘어가면 다시 A로 돌리기 (0~25)
            # 4. +ord('A') : 65를 더해 다시 아스키코드로 돌림
            answer += chr((ord(ch) - ord('A') + n) % 26 + ord('A'))
        elif 'a' <= ch <= 'z':
            answer += chr((ord(ch) - ord('a') + n) % 26 + ord('a'))
            
    return answer