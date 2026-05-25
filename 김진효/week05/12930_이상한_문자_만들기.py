 # [성능 요약] 메모리: 9.16 MB 시간: 0.04 ms 

def solution(s):
    answer = ''

    s = ' ' + s + ' '
    flag = -1
    for idx in range(len(s)):

        #  공백이면 그대로 포함
        if s[idx]==' ':
            answer += ' '
            flag = -1
            continue

        #  첫 글자면 flag 활성화
        if s[idx-1] == ' ':
            flag = 0
            
        if flag % 2 == 0:
            answer += s[idx].upper()
        else:
            answer += s[idx].lower()
            
        flag +=1 
           
    return answer[1:-1]

print(solution("try hello world"))