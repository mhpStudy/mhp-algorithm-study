 # [성능 요약] 메모리: 8.98 MB 시간: 0.01 ms 

def solution(s):
    answer = ''
    sl = s.split(" ")
    for word in sl:
        answer += word.capitalize() + " "
    return answer[:len(answer)-1]