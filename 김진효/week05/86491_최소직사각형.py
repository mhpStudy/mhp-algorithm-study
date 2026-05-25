 # [성능 요약] 메모리: 10.3 MB 시간: 1.98 ms 

def solution1(sizes):
    answer = 0
    # 최대값을 먼저 찾고
    # 최대값을 찾으면 그 반대편 arr에서 상대보다 작으면서 max인걸 고르기
    max_idx, max_v = 0, 0
    arr = []
    for i in range(len(sizes)):
        if sizes[i][0] > sizes[i][1]:
            arr.append(sizes[i][1])
            if sizes[i][0] > max_v:
                max_v = sizes[i][0]
                max_idx = i
        else:
            arr.append(sizes[i][0])
            if sizes[i][1] > max_v:
                max_v = sizes[i][1]
                max_idx = i

    arr.sort(reverse=True)

    answer = max_v * arr[0]
    
    return answer

 # [성능 요약] 메모리: 10.4 MB 시간: 1.42 ms 
def solution(sizes):
    m1 = 0
    m2 = 0
    for w, h in sizes:
        if w < h:
            w,h = h,w
        
        m1 = max(m1,w)
        m2 = max(m2,h)  

    return m1*m2

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))