# 좌표 정렬하기 실버5

import sys
input = sys.stdin.readline
N = int(input())
lis = []
for _ in range(N):
    lis.append(int(input()))

lis.sort()

for num in lis:
    print(num)