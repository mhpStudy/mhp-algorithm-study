# 문제: 동명 동물 수 찾기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/59041

SELECT animal_id, name 
FROM animal_ins 
WHERE animal_type = 'Dog' AND LOWER(name) LIKE '%el%' 
ORDER BY name, animal_id;