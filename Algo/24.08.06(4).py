# 백준 15666 N과 M (12) 실버2

import sys
input = sys.stdin.readline

def dfs(x, N_list):
    if len(res) == M:
        print(*res)
        return

    for i in range(x, len(N_list)):
            res.append(N_list[i])
            dfs(x, N_list)
            res.pop()
            x += 1


    return


N, M = map(int, input().strip().split())
N_list = list(map(int, input().split()))
res = []
visited = [0] * (N+1)
N_list = set(N_list)
N_list = list(N_list)
N_list.sort()
dfs(0, N_list)

# 정확한 재귀호출 과정을 이해하게 된 것 같다.
# 처음에 중복 없애고 (sort는 순서 안중요) 
# 그 다음에 시작 범위를 x로 하고 1씩 높이면서 그 다음 재귀호출에 전달
# 그러면 1계층에서 2계층 까지 x가 동일하고 3계층에서 print를 찍는다
# 4 2
# 9 7 9 1 테케 기준
# 그리고 먼저 print를 찍으므로써 그 전 계층으로 돌아가고 거기서 for문이 다돌아서 또 그 전 계층으로 돌아가고
# 그 때 x가 1씩 증가 
# 증가한 x의 값을 다시 그 다음 계층 호출할 때 넣고 해당 상태에서 과정이 반복되는 것
# 계속 빡치게 뭔가 살짝씩 이해가 안가서 넌 내가 진짜 반드시 이해한다 이생각으로 쓰면서 했더니 완벽 이해된듯
# 진짜 나한테 까불지마라 알고리즘 ㅈ되는 수가 있다 너 