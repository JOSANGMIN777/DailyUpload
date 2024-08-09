# 백준 1932 정수 삼각형 실버2

import sys
input = sys.stdin.readline

N = int(input())
tri = []
for i in range(N):
    tri.append(list(map(int, input().strip().split())))



for i in range(1,N):
    for j in range(i+1):
        if j == 0:
            tri[i][j] += tri[i-1][j]
        elif j == i:
            tri[i][j] += tri[i-1][j-1]
        else:
            tri[i][j] = max(tri[i-1][j-1], tri[i-1][j]) + tri[i][j]


print(max(tri[N-1]))

# DP문제는 머리가 너무 아프다... 뭔가 쉽게 생각하면 되는데 그게 잘 안된다.
# DP특징이 특히 그래프에서는 약간 해당 인덱스에 필요한 값들을 저장해놓고 필요할 때 필요한 인덱스에서 값들만 뽑아쓰는 느낌인거같은데
# 아직 힘들다... 풀이설명을 보고 구현을 했고, else 부분에 자기 자신 더해주는걸 잊어서 해멨다.

