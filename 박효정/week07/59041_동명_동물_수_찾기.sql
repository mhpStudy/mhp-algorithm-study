-- 문제: 동명 동물 수 찾기
-- URL: https://school.programmers.co.kr/learn/courses/30/lessons/59041

SELECT
    NAME,
    COUNT(*)
FROM
    ANIMAL_INS
WHERE
    NAME IS NOT NULL
GROUP BY
    NAME
HAVING
    COUNT(*) >= 2
ORDER BY 
    NAME;