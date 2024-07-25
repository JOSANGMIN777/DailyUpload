# 17219 비밀번호 찾기 실버4

import sys

N, M = map(int, input().split())

List = dict()
for i in range(N):
    address, pw = sys.stdin.readline().strip().split()
    List[address] = pw


for j in range(M):
    Key = input()
    print(List[Key])

# 실버치고 굉장히 쉬운 문제
# 처음에 stdin 특유의 입력시 개행때문에 틀렸는데 처음 input변수 선언할 때 strip을 적용해서 아예 없애버리는 방법이없나 찾아보다가
# 결국 못찾아서 개행 지울 부분에만 저렇게 길게 써줬음.