# 문제: 조건에 맞는 사용자와 총 거래금액 조회하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/164668

SELECT
    U.USER_ID,
    U.NICKNAME,
    SUM(B.PRICE) AS TOTAL_SALES
FROM
    USED_GOODS_BOARD B
JOIN 
    USED_GOODS_USER U
ON 
    B.WRITER_ID = U.USER_ID
WHERE
    B.STATUS = 'DONE'
GROUP BY
    U.USER_ID, U.NICKNAME
HAVING
    SUM(B.PRICE) >= 700000
ORDER BY
    TOTAL_SALES;
