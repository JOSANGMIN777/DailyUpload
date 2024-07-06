# 11650 좌표 정렬하기 실버5

import sys
input = sys.stdin.readline

N = int(input())
List = []
for i in range(N):
    List.append(list(map(int, input().split())))

ans = sorted(List, key=lambda x: (x[0],x[1]))

for i,j in ans:
    print(i, j)

# lambda를 잘 쓰자 굉장히 유용하다 sorted(list, key=lambda x: (몇번째 요소))