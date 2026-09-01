# 문제: 대여 기록이 존재하는 자동차 리스트 구하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/157341

-- SELECT DISTINCT
--     C.CAR_ID
-- FROM
--     CAR_RENTAL_COMPANY_CAR C
-- JOIN 
--     CAR_RENTAL_COMPANY_RENTAL_HISTORY H ON C.CAR_ID = H.CAR_ID
-- WHERE
--     TO_CHAR(H.START_DATE, 'YYYY-MM') = '2022-10'
--     AND C.CAR_TYPE = '세단'
-- ORDER BY
--     C.CAR_ID DESC;

SELECT
    C.CAR_ID
FROM 
    CAR_RENTAL_COMPANY_CAR C
WHERE 
    C.CAR_TYPE = '세단'
    -- EXISTS로 존재 여부만 확인 (JOIN처럼 중복이 생기지 않음)
    -- JOIN: CAR1과 관련된 대여기록을 각각 다 보여줌 10/1, 10/2, 10/3
    -- EXISTS: CAR1에게 대여기록이 있는지만 확인함 -> 있음(TRUE) -> 1행
    AND EXISTS (
        SELECT 1
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY H
        WHERE 
            H.CAR_ID = C.CAR_ID -- 서브쿼리 안에서 바깥 테이블과 연결하는 조건
            AND TO_CHAR(H.START_DATE, 'YYYY-MM') = '2022-10'
    )
ORDER BY
    C.CAR_ID DESC;
