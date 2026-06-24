# 문제: 완주하지 못한 선수
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/42576

'''
["mislav", "stanko", "mislav", "ana"]
["stanko", "ana", "mislav"]
'''
def solution(participant, completion):
    players = {}
    
    for name in participant:
        players[name] = players.get(name, 0) + 1
    
    for name in completion:
        players[name] -= 1
    
    for name in participant:
        if players[name] > 0:
            return name