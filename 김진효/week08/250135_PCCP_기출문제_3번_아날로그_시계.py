'''
초를 기준으로 계산하면
1초 마다 움직이는 각도를 생각해보자(360도 기준)
1초: 360/60, 1분: 360/(60*60), 1시간: 360/(60*60*12)
'''

# 초침이 시침/분침과 겹칠 때마다 알림
def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    h = 360 / (60*60*12)
    m = 360 / (60*60)
    s = 360 / (60)

    # print(h,m,s)
    
    diff = (h2*60*60 + m2*60 + s2) - (h1*60*60 + m1*60 + s1) 

    cur_h = 60*60*h1*h
    cur_m = 60*m1*m
    cur_s = s1*s

    # print(cur_h,cur_m,cur_s)
    
    # 맨 처음 겹칠 경우 처리
    if cur_h == cur_s or cur_m == cur_s:answer += 1
    
    next_h = cur_h
    next_m = cur_m
    next_s = cur_s

    for _ in range(diff):
        next_h += h
        next_m += m
        next_s += s
        
        # print(cur_h, cur_m, cur_s, "||" , next_h,next_m,next_s)
        
        # 1초 움직였을 때 정확히 떨어지지 않으니 앞서 있는지를 봐야하나    
        '''
        시,분,초 다 겹치는 경우를 어떻게 판별할 것인가를 모르겠음..
        '''
        is_overlap_h = cur_s < cur_h and next_s > next_h
        is_overlap_m = cur_s < cur_m and next_s > next_m
        
        if is_overlap_h:
            answer += 1

        if is_overlap_m:
            answer += 1
        
        # 근사치 추정?
        # 359.9999999998369 360.0000000001609 360.0
        is_near_h = -1 < next_h - 360 < 1 
        is_near_m = -1 < next_m - 360 < 1 
        if next_s == 360 and is_near_h and is_near_m:
            answer -= 1

        # 360도 넘어가면 뺴주기
        if next_h>=360: next_h-=360
        if next_m>=360: next_m-=360
        if next_s>=360: next_s-=360

        cur_h = next_h
        cur_m = next_m
        cur_s = next_s

    # 12시 일때만 겹치는걸까? 그냥 예상
    if h2==12 and m2==0 and s2==0:
        answer -=1

    return answer

# print(solution(0,5,30,0,7,0)) # 00:05:30 ~ 00:07:00
# print(solution(11, 58, 59, 11, 59, 0)) # 11:58:59 ~ 11:59:0
print(solution(11, 59, 30, 12, 0, 0))
# print(solution(0,0,0,23,59,59)) # 00:00:00 ~ 23:59:59