# 문제: 같은 숫자는 싫어
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    ans = [arr[0]] # 첫 인덱스는 그냥 넣어둠

    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            ans.append(arr[i])
        
    return ans

'''
    stack = []
    
    for num in arr:
        if not stack or stack[-1] != num:
            stack.append(num)
    
    return stack

'''