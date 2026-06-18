# 문제: [PCCP 기출문제] 3번 / 아날로그 시계
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/250135

def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    M = 43200  # 360도 * 120, 소수 방지용 단위

    # 시작 시간과 끝 시간을 초 단위로 변환
    start = h1 * 3600 + m1 * 60 + s1
    end = h2 * 3600 + m2 * 60 + s2

    # 시작 시간이 00:00:00 또는 12:00:00이면 세 침이 겹침 +1
    if start % 43200 == 0:
        answer += 1

    # 시작부터 끝 직전까지 
    # t초 ~ t+1초 사이에 초침이 분침/시침을 지나는지 확인
    for t in range(start, end):
        # t초 각도
        s_cur = (t * 720) % M   # t * 6도 * 120
        m_cur = (t * 12) % M    # t * 0.1도 * 120
        h_cur = t % M           # t * 1/120도 * 120
        
        # t + 1 초 각도
        s_next = ((t + 1) * 720) % M
        m_next = ((t + 1) * 12) % M
        h_next = (t + 1) % M
        
        # 초침 기준으로 분침이 얼마나 앞에 있는지
        # 분침 - 초침 상대각도
        cur_m = (m_cur - s_cur) % M
        next_m = (m_next - s_next) % M

        # 초침 기준으로 시침이 얼마나 앞에 있는지
        # 시침 - 초침 상대각도
        cur_h = (h_cur - s_cur) % M
        next_h = (h_next - s_next) % M

        # cur_m > 0: 현재 초침보다 더 앞에 있음
        # next_m > cur_m : 다음 순간 상대각도가 커짐 
        # 초침이 항상 더 빠르므로 상대각도는 이전보다 언제나 줄어야 함 
        # 상대각도가 늘어났다는건 감소하던 값이 0을 지나 음수가 되었고, %연산으로 큰 값으로 변한 것
        # next_m == 0 : 일치하는 순간
        if cur_m > 0 and (next_m > cur_m or next_m == 0):
            answer += 1

        if cur_h > 0 and (next_h > cur_h or next_h == 0):
            answer += 1

        if (t + 1) % 43200 == 0:
            answer -= 1

    return answer