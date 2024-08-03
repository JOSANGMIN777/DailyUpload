# 백준 15652 N과M(4) 실버3

import sys
input = sys.stdin.readline

def dfs(X):
    if len(res) == M:
        print(*res)
        return

    for num in range(X, N+1):
        res.append(num)
        dfs(num)
        res.pop()

N,M = map(int,input().split())
res = []
dfs(1)

# 여기에 dfs를 쓰게 될 줄은 블로그 보기전에 상상도 못했다. 
# 수열조합만 주구장창 따지다가 막혀서 참고하게 됐다.
# dfs재귀의 특성에 대해 잘알아야 풀 수 있는 문제이며 간략히 설명하자면
# 리스트에 값을 추가하고 재귀 호출을하고 리스트의 길이가 M과 같아지면 해당 값을 프린트하고 리턴한다.
# 그러면 해당 dfs함수가 끝나고 그 전에 호출되었던 함수로 돌아간다. 
# 거기서 dfs(num) 아래에 있는 pop이 실행되고 그 다음 수가 추가된다. 
# 그러다가 마지막 부분에서 N+1 범위까지 다 돌게되면 for문이 끝나면서 그 전 함수 호출로 가게되고
# 거기서 pop이 여러번 되면서 자릿수를 비우고 위 과정을 계속 반복하게 된다. 