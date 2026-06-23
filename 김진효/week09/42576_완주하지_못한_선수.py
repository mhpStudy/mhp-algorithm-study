# [성능 요약] 메모리: 30.4 MB 시간: 43.32 ms 

def solution(participant, completion):
    answer = ''
    com_map = {}
    
    for com in completion:
        if com_map.get(com):
            com_map[com] += 1
        else:
            com_map[com] = 1
    
    
    for par in participant:
        if com_map.get(par):
            com_map[par] -= 1
        else:
            answer = par

    return answer

# print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))