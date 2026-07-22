# 문제: 중복 제거하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/59408

SELECT
    COUNT(DISTINCT NAME) -- COUNT는 NULL인 컬럼 제외하고 셈
FROM
    ANIMAL_INS;