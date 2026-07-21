def solution(name):
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    num = 0

    for i in name:
        if alphabets.index(i) <= 13:
            num += alphabets.index(i)
        elif alphabets.index(i) > 13:
            num += 26 - alphabets.index(i)
            
    n = len(name)
    move = n - 1
    
    for i in range(n):
        next_i = i + 1
        while next_i < n and name[next_i] == "A":
            next_i += 1
        
        move = min(move, i + i + (n - next_i), i + (n - next_i) * 2)
        
    return num + move