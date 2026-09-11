# 문제: 3월에 태어난 여성 회원 목록 출력하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/131120

SELECT
    member_id,
    member_name,
    gender,
    TO_CHAR (date_of_birth, 'YYYY-MM-DD') as "DATE_OF_BIRTH"
FROM member_profile
WHERE
    TO_CHAR (date_of_birth, 'MM') = '03'
    AND GENDER = 'W'
    AND tlno IS NOT NULL
ORDER BY member_id asc;