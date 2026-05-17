# [성능 요약] 메모리: 9.36 MB 시간: 8.69 ms
# 정확성: 69.5 효율성: 30.5, 합계: 100.0 / 100.0

def solution(s):
    # '('를 만나면 stack에 쌓고 ')' 를 만나면 '(' 꺼내기
    # 올바른 괄호가 아닌 상황
    # -> stack 에서 '(' 꺼내려고 했는데 없음
    # -> 마지막에 stack 에 '(' 가 남아있음

    answer = True
    stack = []

    if s[0] == ')':
        return False

    for i in range(len(s)):
        if s[i] == "(":
            stack.append(s[i])
        else:
            if stack:
                stack.pop()
            else:
                return False

    if stack:
        return False

    return True

# [성능 요약] 메모리: 10 MB 시간: 7.11 ms
# 정확성: 69.5 효율성: 30.5
# 흠 비슷하게 나왔네..?
def solution2(s):
    answer = True

    if s[0] == ')':
        return False

    stack = [''] * len(s)
    top = -1

    for c in s:
        if c == "(":
            top += 1
            stack[top] = c
        else:
            if top > -1:
                top -= 1
            else:
                return False

    if top > -1:
        return False

    return True


print(solution('()()'))
print(solution('(())()'))
print(solution(')()('))
print(solution('(()('))

