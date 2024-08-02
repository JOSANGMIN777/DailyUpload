# 백준 15654 N과 M(5) 실버3

import sys, itertools
input = sys.stdin.readline

N,M = map(int,input().strip().split())
perms = list(map(int,input().split()))

res = []
for p in itertools.permutations(perms, M):
    res.append(p)
res = sorted(res, key= lambda x: x )

for i in res:
    print(*i)

# permutations 사용하는 부분에서 시간초과가 나지 않을까 걱정했지만
# 다행히 발생하지 않았고 1제출로 솔했다. 실버문제는 이제 솔직히 웬만하면 다 푸는거 같은데 골드가 문제여... BFS랑... 해보자 계속
