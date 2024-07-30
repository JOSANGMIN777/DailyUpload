# 9375 자칭 패션왕 시발 신해빈년 실버3

import sys
from collections import Counter
input = sys.stdin.readline


N = int(input())
for i in range(N):
    closet = {}
    M = int(input())

    for j in range(M):
        name, type = input().strip().split()

        if not type in closet:
            closet[type] = 1
        else:
            closet[type] += 1
    cnt = 1

    for k in closet:
        cnt *= (closet[k] + 1)
    print(cnt-1)

# 개빡치는점 이딴걸 못풀었다는 점
# 결국 남의 코드를 참조했다. 수학적 이해가 아직 내가 굉장히 부족한것같다.
# 난 아직도 왜 다 입는 경우를 생각안하는지 모르겠다. 만약 상의 3개 하의 2개라고 했을 때 상의만 입는경우 3 하의만 입는경우 2 둘 다 입는경우가 6 그래서 11이 나오는건데
# 죄다 이걸 무슨 각 종류에 1을 더하고 모두 다 입는경우 하나를 빼서 계산한다 이지랄을 떨고 있다.
# 그냥 종류별로 몇갠지 세고 그거 다 곱하고 각각의 종류별 수를 더하면 될텐데 
# 근데 이걸 구현할 때 위 처럼 하면 너무 복잡해짐
# 그래서 그냥 각 종류에 1더하고 마지막에 하나 빼는걸로 하는거같은데 난 왜 이해가 안될까 이게 그냥 외우고 넘어가자