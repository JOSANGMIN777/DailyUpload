# 1620 나는야 포켓몬 마스터 이다솜 실버4

import sys

N,M = map(int, input().split())
pocket = dict()
numbers = dict()
for i in range(1,N+1):
    name = sys.stdin.readline().strip()
    pocket[name] = i
    numbers[i] = name
for i in range(M):
    ans = sys.stdin.readline().strip()
    if ans.isdigit():
        ans = int(ans)
        print(numbers[ans])
    else:
        print(pocket[ans])

# 전형적인 씹관종 문제고 출제자가 개오덕인듯
# 처음에 k,v를 인자로 하는 for문을 딕셔너리에서 돌았다가 시간초과가 났음
# 그래서 그냥 딕셔너리를 숫자용 하나, 이름용 하나 총 두개를 만들어서 푸니까 맞았음.