# 문제: 조건별로 분류하여 주문상태 출력하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/131113

SELECT
    ORDER_ID,
    PRODUCT_ID,
    TO_CHAR(OUT_DATE, 'YYYY-MM-DD') AS OUT_DATE,
    CASE 
        WHEN OUT_DATE IS NULL THEN '출고미정'
        WHEN OUT_DATE <= DATE '2022-05-01' THEN '출고완료'
        ELSE '출고대기'
    END AS 출고여부
FROM
    FOOD_ORDER
ORDER BY
    ORDER_ID;