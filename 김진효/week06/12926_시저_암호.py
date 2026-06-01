# [성능 요약] 메모리: 9.27 MB 시간: 0.89 ms 

def solution(s, n):
    answer = ''
    lower_number = ord('a') 
    uppper_number = ord('A')
    for c in s:
        if c == " ":
            answer += " "
        else:
            target = ord(c)

            if target - lower_number >= 0:
                target -= lower_number
                answer += chr((target+n) % 26 + lower_number)
            else:
                target -= uppper_number
                answer += chr((target+n) % 26 + uppper_number) 

    return answer

print(solution("a B z", 4))