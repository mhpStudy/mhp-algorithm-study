# 문제: 조건별로 분류하여 주문상태 출력하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/131113

SELECT
    order_id,
    product_id,
    TO_CHAR (out_date, 'YYYY-MM-DD') as "OUT_DATE",
    (
        CASE
            WHEN out_date < TO_DATE ('2022-05-02', 'YYYY-MM-DD') THEN '출고완료'
            WHEN out_date > TO_DATE ('2022-05-01', 'YYYY-MM-DD') THEN '출고대기'
            ELSE '출고미정'
        END
    ) as "출고여부"
FROM food_order
ORDER BY order_id asc;

-- 테스트 결과와 정확히 맞추려면 null로 뜨는 값 처리 해줘야함
SELECT order_id, product_id, NVL (
        TO_CHAR (out_date, 'YYYY-MM-DD'), ''
    ) as "OUT_DATE", (
        CASE
            WHEN out_date < TO_DATE ('2022-05-02', 'YYYY-MM-DD') THEN '출고완료'
            WHEN out_date > TO_DATE ('2022-05-01', 'YYYY-MM-DD') THEN '출고대기'
            ELSE '출고미정'
        END
    ) as "출고여부"
FROM food_order
ORDER BY order_id asc;