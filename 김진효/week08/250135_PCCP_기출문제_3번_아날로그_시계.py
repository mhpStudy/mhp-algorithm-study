
'''
-- 1차 시도 실패

초를 기준으로 계산하면
1초 마다 움직이는 각도를 생각해보자(360도 기준)
1초: 360/60, 1분: 360/(60*60), 1시간: 360/(60*60*12)
'''

# # 초침이 시침/분침과 겹칠 때마다 알림
# def solution(h1, m1, s1, h2, m2, s2):
#     answer = 0
#     h = 360 / (60*60*12)
#     m = 360 / (60*60)
#     s = 360 / (60)

#     # print(h,m,s)
    
#     diff = (h2*60*60 + m2*60 + s2) - (h1*60*60 + m1*60 + s1) 

#     # 초기값
#     total_start = h1 * 60 * 60 + m1 * 60 + s1

#     cur_h = total_start % (12 * 60 * 60) * h
#     cur_m = total_start % (60 * 60) * m
#     cur_s = total_start % 60 * s 

#     # print(cur_h,cur_m,cur_s)
    
#     # 맨 처음 겹칠 경우 처리
#     if cur_h == cur_s or cur_m == cur_s:answer += 1
    
#     next_h = cur_h
#     next_m = cur_m
#     next_s = cur_s

#     for _ in range(diff):
#         next_h += h
#         next_m += m
#         next_s += s
        

#         # print(cur_h, cur_m, cur_s, "||" , next_h,next_m,next_s)
        
#         # 1초 움직였을 때 정확히 떨어지지 않으니 앞서 있는지를 봐야하나    
#         is_overlap_h = cur_s < cur_h and next_s > next_h
#         is_overlap_m = cur_s < cur_m and next_s > next_m
        
#         if is_overlap_h:
#             answer += 1

#         if is_overlap_m:
#             answer += 1
        
#         # 360도 넘어가면 뺴주기
#         if next_h>=360: 
#             next_h-=360
#             # 셋 다 겹칠 경우(정각일때) 처리
#             answer -= 1
#         if next_m>=360: next_m-=360
#         if next_s>=360: next_s-=360

#         cur_h = next_h
#         cur_m = next_m
#         cur_s = next_s

#     return answer


'''
 # [성능 요약] 메모리: 11.6 MB 시간: 11.47 ms 
2차시도: 1초에 1/120, 1/10, 6 만큼 움직이까 부동소수점 오류 해결을 위해 120씩 곱해서 정수로 맞춰주자
그렇게 되면 360 * 120 ==  43200 
이 시계 한 턴을 43200 으로 보면 된다
'''
def solution(h1, m1, s1, h2, m2, s2):
    answer = 0

    base = 43200

    # 각 '시, 분, 초' 가 움직이는 각도
    h = base // (60*60*12) 
    m = base // (60*60) 
    s = base // (60)
    # print(h,m,s)

    # 시작점과 끝점
    start = h1*60*60 + m1*60 + s1
    end = h2*60*60 + m2*60 + s2

    # 시간 차이
    diff = end - start

    # 시작점을 일단 맞춰두고 그 뒤에 움직인 각도 구하기
    # 시작점이라는게 각 시, 분, 초 가 움직인게 아니고
    # 시침 기준이면 분침, 초침이 움직이면서 시침 또한 가만히 있지 않고 움직였을 거임
    # 따라서 시작점을 다른 것에 영향을 받아 움직인걸 반영을 해줘야한다
    cur_h = start * h % base
    cur_m = start * m % base
    cur_s = start * s % base

    # 맨 처음 겹칠 경우 처리
    if cur_h == cur_s or cur_m == cur_s:answer += 1
    
    next_h = cur_h
    next_m = cur_m
    next_s = cur_s

    # 1초마다 움직이면서 확인해보자
    for _ in range(diff):
        next_h += h 
        next_m += m 
        next_s += s

        # print(cur_h, cur_m, cur_s, "||" , next_h,next_m,next_s)
        
        #  초침이 시침 이전에 있었는데 이후 시침 앞에 왔다면 제친 경우 -> 겹쳤을 것 
        if cur_s < cur_h and next_s >= next_h:
            answer += 1

        #  초침이 분침 이전에 있었는데 이후 분침 앞에 왔다면 제친 경우 -> 겹쳤을 것 
        if cur_s < cur_m and next_s >= next_m:
            answer += 1

        # 셋 다 겹치는 경우는 정각일 때 -> 각도가 43200 일 때 (한바퀴 넘어가면 빼주는건 아래에서 하므로)
        if next_h  == next_m == next_s :
            # print(next_h,next_m,next_s)
            answer -= 1

        # 한 바퀴 넘어가면 빼주기
        if next_h>=base: next_h-=base
        if next_m>=base: next_m-=base
        if next_s>=base: next_s-=base

        # 값 갱신
        cur_h = next_h
        cur_m = next_m
        cur_s = next_s
    
    return answer

print(solution(0,5,30,0,7,0)) # 00:05:30 ~ 00:07:00
print(solution(11, 58, 59, 11, 59, 0)) # 11:58:59 ~ 11:59:0
print(solution(11, 59, 30, 12, 0, 0))
print(solution(0,0,0,23,59,59)) # 00:00:00 ~ 23:59:59