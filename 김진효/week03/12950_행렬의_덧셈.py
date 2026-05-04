 # [성능 요약] 메모리: 22 MB 시간: 32.21 ms 

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr1[i])):
            temp.append(arr1[i][j]+arr2[i][j])
        answer.append(temp)
    return answer