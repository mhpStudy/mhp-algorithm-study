# 문제: 중복 제거하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/59408

SELECT COUNT(DISTINCT name) 
FROM animal_ins 
WHERE name IS NOT NULL;

SELECT COUNT(*)
FROM (
        SELECT DISTINCT
            name
        FROM animal_ins
        WHERE
            name IS NOT NULL
    );