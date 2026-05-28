# 문제: 짝지어 제거하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12973

# 시간초과로 터짐
# def solution(s):
#     answer = 0
    
#     while s: # 전부 제거할때까지 반복
#         # 이전 알파벳
#         a = s[0]
#         # s의 길이
#         l = len(s)
        
#         for i in range(1, len(s)):
#             # 다음 알파벳이 다르다면, a 갱신하고 다음 인덱스 확인 (continue)
#             if a != s[i]:
#                 a = s[i]
#                 continue
                
#             # 같은 알파벳이 붙어있다면
#             else:
#                 # 같은 알파벳 제거하고 새 문자열로 다시 검사 시작 (break)
#                 s = s[:i-1] + s[i+1:]
#                 break
        
#         # 처리가 끝난 후 길이가 이전과 같다면 반복 종료
#         if l == len(s):
#             break

#     if not len(s):
#         answer = 1
    
#     return answer

def solution(s):
    stack = []
    
    for char in s:
        # 스택이 비어있지 않고, top 글자가 현재 글자와 같다면
        if stack and stack[-1] == char:
            stack.pop() # 제거
        else:
            stack.append(char)
    
    return 0 if stack else 1