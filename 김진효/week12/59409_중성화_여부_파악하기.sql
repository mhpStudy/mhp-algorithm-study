# 문제: 중성화 여부 파악하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/59409

SELECT
    animal_id,
    name,
    CASE
        WHEN sex_upon_intake LIKE '%Neutered%'
        OR sex_upon_intake LIKE '%Spayed%' THEN 'O'
        ELSE 'X'
    END AS "중성화"
FROM animal_ins
ORDER BY animal_id;