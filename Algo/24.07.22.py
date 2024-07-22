# 12847 꿀 아르바이트 실버3

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
T = list(map(int,input().split()))


window = sum(T[:m])
ans = window

for i in range(m, n):
    window += T[i] - T[i-m]
    ans = max(ans, window)

print(ans)

# 슬라이딩 위도우를 활용하여 풀면 된다.