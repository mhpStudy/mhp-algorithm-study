 # [성능 요약] 메모리: 39.5 MB 시간: 57.02 ms 
def solution(phone_book):
    len_arr = set()     # 문자열 길이만 저장할 set
    phone_dic = {}      # 문자열 저장할 dict

    # 문자열 길이와 문자열 다 저장해버리기
    for i in range(len(phone_book)):
        len_arr.add(len(phone_book[i]))
        phone_dic[phone_book[i]] = 1

    # 전화번호 돌면서
    for i in range(len(phone_book)):
       # 길이 만큼 잘라볼거임
       for l in len_arr:
        #  자르려는 길이가 더 길거나 같다? 그러면 pass
        if l >= len( phone_book[i]): continue
        # 자른 문자열이 dict에 있는지 확인
        if phone_dic.get(phone_book[i][:l]):
            return False
    
    return True

''' 시간초과 '''
# def solution(phone_book):
#     phone_book.sort(key = lambda i : len(i))

#     for i in range(len(phone_book)):
#         for j in range(len(phone_book)-1,i, -1):
#             if phone_book[j].startswith(phone_book[i]):
#                 return False
#     return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12","123","1235","567","88"]))