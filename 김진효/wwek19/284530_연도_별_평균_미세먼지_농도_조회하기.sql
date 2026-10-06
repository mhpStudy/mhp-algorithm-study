# 문제: 연도 별 평균 미세먼지 농도 조회하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/284530

-- 지역구분1, 지역구분2, 측정일, 미세먼지 오염도, 초미세먼지 오염도
-- 수원 지역 / 연도 별 평균 미세먼지 오염도 / 평균 초미세먼지 오염도
SELECT YEAR(ym) as "YEAR", ROUND(AVG(pm_val1), 2) as "PM10", ROUND(AVG(pm_val2), 2) as "PM2.5"
FROM air_pollution
WHERE
    location2 = "수원"
GROUP BY
    YEAR(ym)
ORDER BY year asc;