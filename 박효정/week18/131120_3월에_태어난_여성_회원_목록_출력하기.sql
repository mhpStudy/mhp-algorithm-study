# 문제: 3월에 태어난 여성 회원 목록 출력하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/131120

SELECT
    MEMBER_ID,
    MEMBER_NAME,
    GENDER,
    TO_CHAR(DATE_OF_BIRTH, 'YYYY-MM-DD') AS DATE_OF_BIRTH
FROM
    MEMBER_PROFILE
WHERE
    GENDER = 'W'
    AND
    TO_CHAR(DATE_OF_BIRTH, 'MM') = '03'
    AND
    TLNO IS NOT NULL
ORDER BY
    MEMBER_ID;