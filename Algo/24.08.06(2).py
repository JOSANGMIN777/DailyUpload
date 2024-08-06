# 백준 15650 N과 M(2) 실버3
 
import sys
input = sys.stdin.readline

def dfs(x):
    if len(res) == M:
        print(*res)
        return

    for i in range(x, N+1):
        if visited[i] == 0:
            visited[i] = 1
            res.append(i)
            dfs(i)
            res.pop()
            visited[i] = 0
    return

N,M = map(int,input().split())
res = []
visited = [0]*(N+1)
dfs(1)

# 전형적인 dfs문제로 visited배열을 사용하고 다시 초기화 해주어야하는 문제였다.
# 뭔가 풀긴했는데 때려 맞춘거같은 찜찜함이 남아서 다시 그 흔적을 추적해봤다.
# 호출의 단계에 대해서 정확히 파악하고 있어야 이해할 수 있는데 
# 2번 테케의 경우, 2번째 호출 단계에서 배열의 길이가 2가 되므로 출력이 되고 pop되고 visited초기화 되기를 반복한다.
# 그리고 1번째 호출 단계에 돌아와서 for문의 인덱스가 i++ 되면서 더 작은 수는 아예 출력조차 되지 않는 것이고, 중복없이 또 다시 2번째 호출단계에서
# 출력을 반복하고 이 과정이 마지막 인덱스까지 지속되는것이다.