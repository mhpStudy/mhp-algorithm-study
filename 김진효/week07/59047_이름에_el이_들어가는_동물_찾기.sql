# 문제: 이름에 el이 들어가는 동물 찾기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/59047

SELECT name, COUNT(name) as COUNT 
FROM animal_ins 
GROUP BY name 
HAVING COUNT(name) >= 2 
ORDER BY name;