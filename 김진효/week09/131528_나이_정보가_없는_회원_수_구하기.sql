# 문제: 나이 정보가 없는 회원 수 구하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/131528


SELECT COUNT(CASE WHEN age IS NULL THEN 1 END) as "USERS" FROM user_info

SELECT COUNT(*) as "USERS"
FROM (
        SELECT age
        FROM user_info
        WHERE
            age IS null
    )