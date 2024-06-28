# 1181 단어 정렬 실버5

import sys
input = sys.stdin.readline

N = int(input())
chars = []
for i in range(N):
    chars.append(input())
Set = list(set(chars))


Set.sort()
Set = sorted(Set, key = lambda x: len(x) )
for ch in Set:
    print(ch.strip())
