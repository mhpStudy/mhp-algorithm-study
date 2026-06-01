# [성능 요약] 메모리: 11.3 MB 시간: 0.01 ms 

def solution(s):
    dic = {"zero":"0","one":"1","two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    
    for k in dic.keys():
        if s.find(k) > -1:
            s = s.replace(k,dic.get(k))

    return int(s)

print(solution("one4seveneight"))