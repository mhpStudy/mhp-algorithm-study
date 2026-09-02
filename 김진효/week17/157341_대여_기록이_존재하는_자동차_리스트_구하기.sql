# 문제: 대여 기록이 존재하는 자동차 리스트 구하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/157341

-- 자동차 종류가 '세단'인 자동차들 중 10월에 대여를 시작한 기록이 있는 자동차 ID 리스트를 출력
SELECT DISTINCT (rc.car_id) as "CAR_ID"
FROM
    car_rental_company_car rc
    JOIN car_rental_company_rental_history rh ON rc.car_id = rh.car_id
WHERE
    rc.car_type = '세단'
    and TO_CHAR (rh.start_date, 'MM') = '10'
ORDER BY 1 desc;