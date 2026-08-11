# 문제: 조건에 맞는 도서와 저자 리스트 출력하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/144854


-- WHERE 절 이용
SELECT b.book_id, a.author_name, TO_CHAR(b.published_date,'YYYY-MM-DD') as "PUBLISHED_DATE" FROM book b, author a 
WHERE 
b.author_id = a.author_id
AND
b.category = '경제' ORDER BY b.published_date;


-- JOIN 이용
SELECT b.book_id, a.author_name, TO_CHAR (
        b.published_date, 'YYYY-MM-DD'
    ) as "PUBLISHED_DATE"
FROM book b
    JOIN author a ON b.author_id = a.author_id
WHERE
    b.category = '경제'
ORDER BY b.published_date;