 # [성능 요약] 메모리: 27 MB 시간: 107.34 ms 

def solution(arr):
    answer = [arr[0]]
    for i in range(1,len(arr)):
        if arr[i] == arr[i-1]:
            continue
        answer.append(arr[i])
        
    return answer