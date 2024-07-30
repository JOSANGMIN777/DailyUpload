# 11279 최대 힙 실버2

import heapq
import sys
input = sys.stdin.readline

heap = []

N = int(input())

for i in range(N):
    X = int(input())
    if X == 0:
        if not heap:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -X)


# 기존의 최대힙 구현방법을 조금 변형하면 풀리는 문제
# 힙에 대한 자신감이 생겼다. 계속 가보자