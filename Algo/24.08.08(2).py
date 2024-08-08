# 백준 11053 가장 긴 증가하는 부분 수열 실버2

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
table = [1] * N

for i in range(1,N):
    for j in range(i):
        if A[i] > A[j]:
            table[i] = max(table[i], table[j]+1)

print(max(table))

# DP인듯 DP아닌 DP같은 문제이다.
# 여기서 가장 중요한건 table[i] = max(table[i], table[j]+1) 이 부분을 떠올릴 수 있냐 없냐이다.
# 이게 진짜 브빌리언트한 코드인게 뭐냐면 저 부분에서 캐싱을 통해 이전 비교까지의 값을 바로바로 불러올 수가 있다는 점이다.
# 만약 배열[i]가 배열[j]보다 크다면 증가하는 부분 수열인 것이며 그렇다면 table[i]에는 배열[i]까지 몇번 증가했는지 현재까지의 기록을 그때마다 넣을 수 있는것이다.
# [10, 20, 10, 30, 20, 50] # 출력 4 이걸 예시로 들었을 때
# i는 1부터든 0부터든 큰 차이는 없다. i가 현재 보고 있는 위치까지 j는 처음부터 i가 현재 보고있는 위치까지 갈 것이다.
# 그러면 배열[i]가 가질 수 있는 최대 부분수열 길이를 기록한 table[i]는 계속 비교를 하면서 커지는데
# 여기서 만약 10, 20 순으로 배열이 돌면서 table[1]에(앞으로 편의상 20이라 하겠다.) 2가 담겨있다고 하자 (처음 [1]*N으로 초기화한 이유는 자기자신이 부분수열에 포함되기 때문)
# 그러면 그 다음에 10 20 10 30을 볼 때는(20과 20 다음의 10을 비교하면 애초에 if문이 충족안하므로 생략 후 그다음으로 넘어감) if문에 의해 i는 30을 보고있고 j는 10부터 열심히 달려간다 30까지
# 여기서 현재 i가 보고 있는 30과 j가 보고있는 값들을 비교하게 될텐데 최초 0번째 인덱스의 10이 조건을 충족하므로 30에는 2가 담기게 된다.
# 그 다음 20도 조건을 충족하므로 20에 있는 2에 1을 더한 값과 30에 담긴 2를 비교하며 더 큰 3이 30에 담기게 된다.
# 이걸 인간의 인식수준으로 생각하면 20이 10보다 크니까 저기서 수열길이 2 그다음 10 20 30 수열길이 3짜리의 부분수열을 만들수 있으니까 30에 3
# 이것과 똑같은 원리인것이다. 다만, 코드로 구현할 때, 우리가 처음부터 다시 셀 필요없이 이미 해당 수가 가지고 있는 증가수열의 길이를 그대로 가져와 추가만 한것이기 때문에 효율성이 높아지는 것이다.