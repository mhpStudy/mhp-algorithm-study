# [성능 요약] 메모리: 10 MB 시간: 1.49 ms 

def solution(s):
    answer = []
    d = {}
    for c in range(ord('a'),ord('z')+1):
        d[chr(c)] = -1

    for i in range(len(s)):
        pre = d.get(s[i])
        if pre == -1:
            answer.append(-1)
        else:
            answer.append(i - pre)
        d[s[i]] = i

    return answer

print(solution("banana"))