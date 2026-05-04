 # [성능 요약] 메모리: 15.1 MB 시간: 2.32 ms 

def solution(arr):
    answer = []
    if len(arr) == 1:
        answer.append(-1)
    else:
        x = min(arr)
        answer = [i for i in arr if i!=x]
    return answer