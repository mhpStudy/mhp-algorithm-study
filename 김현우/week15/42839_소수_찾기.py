# 문제: 소수 찾기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/42839

from collections import Counter

def solution(numbers):
    answer = 0
    # 일단 9999999 까지 모든 소수를 다 찾아두자
    primes = [True] * 10000000
    primes[0] = primes[1] = False
    for i in range(2, int(10000000**0.5)):
        if primes[i]:
            for j in range(i*i, 10000000, i):
                primes[j] = False
    # 숫자 조각이 몇개씩 있나 세어두자
    numbercount = Counter(numbers)
    for i in range(2,10000000):
        if primes[i]:
            primecount = Counter(str(i))
            for item, count in primecount.items():
                if numbercount[item] < count: break
            else: answer += 1
    return answer

# 너무 비효율적임.. 입력된 수 까지만 조사하게 해야겠

'''
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)
    
#############################################################
    
primeSet = set()


def isPrime(number):
    if number in (0, 1):
        return False
    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def makeCombinations(str1, str2):
    if str1 != "":
        if isPrime(int(str1)):
            primeSet.add(int(str1))

    for i in range(len(str2)):
        makeCombinations(str1 + str2[i], str2[:i] + str2[i + 1:])


def solution(numbers):
    makeCombinations("", numbers)

    answer = len(primeSet)

    return answer
'''