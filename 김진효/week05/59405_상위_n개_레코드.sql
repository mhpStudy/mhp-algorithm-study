-- 문제: 상위 n개 레코드
-- URL: https://school.programmers.co.kr/learn/courses/30/lessons/59405

-- oracle
SELECT name FROM animal_ins ORDER BY datetime FETCH FIRST 1 ROWS ONLY;

-- mysql
SELECT name FROM animal_ins ORDER BY datetime LIMIT 1;