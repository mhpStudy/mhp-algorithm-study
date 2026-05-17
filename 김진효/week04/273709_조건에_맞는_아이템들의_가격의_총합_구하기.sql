# 문제: 조건에 맞는 아이템들의 가격의 총합 구하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/273709

SELECT dr_name, dr_id, mcdp_cd, hire_ymd() FROM doctor WHERE mcdp_cd = 'CS' or mcdp_cd = 'GS' ORDER BY hire_ymd desc, dr_name asc;