# 문제: 동명 동물 수 찾기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/59041

SELECT name, COUNT(name) as COUNT 
FROM animal_ins 
GROUP BY name 
HAVING COUNT(name) >= 2 
ORDER BY name;