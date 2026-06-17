# 문제: DATETIME에서 DATE로 형 변환
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/59414

-- Oracle
SELECT animal_id, name, DATEFORMAT (datetime, 'YYYY-MM-DD')
FROM ANIMAL_INS
ORDER BY animal_id

-- MySQL
SELECT animal_id, name, DATE_FORMAT(datetime, '%Y-%m-%d') as "날짜"
FROM ANIMAL_INS
ORDER BY animal_id