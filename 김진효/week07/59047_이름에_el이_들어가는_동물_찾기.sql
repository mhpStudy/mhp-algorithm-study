# 문제: 이름에 el이 들어가는 동물 찾기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/59047

SELECT animal_id, name 
FROM animal_ins 
WHERE animal_type = 'Dog' AND LOWER(name) LIKE '%el%' 
ORDER BY name, animal_id;