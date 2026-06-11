-- 문제: 동명 동물 수 찾기
-- URL: https://school.programmers.co.kr/learn/courses/30/lessons/59041

SELECT NAME, COUNT(NAME) AS COUNT
FROM ANIMAL_INS
GROUP BY NAME
HAVING COUNT > 1
ORDER BY NAME
