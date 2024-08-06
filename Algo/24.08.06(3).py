# 백준 15663 N과 M(9) 실버2

import sys, itertools
input = sys.stdin.readline

N, M = map(int, input().strip().split())
N_list = list(map(int, input().split()))
ans = set()
for p in itertools.permutations(N_list, M):
    ans.add(p)

ans = list(ans)
ans.sort()
for nums in ans:
    print(*nums)

# 솔직히 이게 왜 dfs쓰는 N과 M보다 티어가 높은지 잘 모르겠다.
# 파이썬이 사기인게 set을 그냥 다시 list에 넣으면 list가 된다.
# 코테는 무조건 이걸로 간다. 