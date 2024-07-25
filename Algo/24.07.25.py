# 1927 최소 힙 실버2

import sys
import heapq
input = sys.stdin.readline

heap = []

N = int(input())
for i in range(N):
    X = int(input())
    if X == 0:
        if (heap):
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, X)

# 가장 기본적인 heappush와 heappop을 이용해서 풀면 되는 문제
# 만약 sort, pop 등을 사용해서 풀면 시간초과나 난다.
# 드디어 힙에 도달했다. 여기서 더 더 정진해서 코테를 다 씹어먹자
# 물론 서류가 먼저겠지만... ㅠㅠ