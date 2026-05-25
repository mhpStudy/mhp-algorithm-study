 # [성능 요약] 메모리: 10.6 MB 시간: 81.73 ms 

def solution(s):
    stack = ['-1']

    for i in range(len(s)):
        if s[i] != stack[-1]:
            stack.append(s[i])

        else:
            stack.pop()

    return 1 if stack[-1] == '-1' else 0

print(solution('baabaa'))
print(solution('cdcd'))