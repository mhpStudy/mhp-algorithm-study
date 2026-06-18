-- 문제: DATETIME에서 DATE로 형 변환
-- URL: https://school.programmers.co.kr/learn/courses/30/lessons/59414

SELECT ANIMAL_ID, NAME, DATE(DATETIME) AS '날짜'
3
FROM ANIMAL_INS
4
ORDER BY ANIMAL_ID