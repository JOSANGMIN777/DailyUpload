# 백준 1149 RGB거리 실버1

import sys
input = sys.stdin.readline

N = int(input())
d = [[0] * 3 for _ in range(N)]
for i in range(N):
    R, G, B = map(int, input().strip().split())
    d[i][0] = R; d[i][1] = G; d[i][2] = B

for i in range(1,N):
    d[i][0] = min(d[i-1][1], d[i-1][2]) + d[i][0]
    d[i][1] = min(d[i-1][0], d[i-1][2]) + d[i][1]
    d[i][2] = min(d[i-1][0], d[i-1][1]) + d[i][2]

print(min(d[N-1]))

# 또 다른 DP문제...
# 아니 생각을 너무 어렵게 하나? 일단 기본적으로 두려움이 좀 있는듯
# 간단하게 풀이하면 되는데 무슨 조건문 써가면서 구현하려다 결국 풀이참조... ㅠㅠ
# 아직 연습이 더 필요한 것 같다
# 그냥 이전꺼에서 값을 추가할 인덱스와 동일 인덱스를 제외한 값 중 min값을 추가하면서 
# 마지막 N-1번 줄에서 min값을 출력하면된다. 하... 좀 잘해보자
# 여차저차해서 골드를 달성했다 드디어 ㅎㅎ 이건 좀 뿌듯
# 다음엔 BFS 조진다.