# 11286 절댓값 힙 실버1

import heapq, sys
input = sys.stdin.readline

N = int(input())
heap = []

for i in range(N):
    X = int(input().strip())

    if X > 0:
        heapq.heappush(heap, (X,X))

    elif X < 0:
        heapq.heappush(heap, (-X,X))

    else:
        if heap:
            first = heapq.heappop(heap)
            print(first)
        else:
            print(0)

# 힙의 신기원! 새로운 발견!
# 힙에 튜플을 넣을 수 있는데, 튜플을 넣을 경우 (a,b) a로 처음 정렬을 하고 a로 정렬되어있는 와중에 b를 기준으로 한번더 정렬한다.
