# 1541 잃어버린 괄호 실버2

import sys
input = sys.stdin.readline

formula = input().strip().split('-')
List = []
for i in formula:
    List.append(i.split('+'))

tmp = []
for i in range(len(List)):
    for j in range(len(List[i])):
        List[i][j] = int(List[i][j])

for i in List:
    tmp.append(sum(i))

cnt = tmp[0]
for i in range(1, len(tmp)):
    cnt -= tmp[i]

print(cnt)

# 아이디어가 도저히 안떠올라서 블로그에서 풀이접근방법을 보고 풀었다.
# 다행히 혼자 힘으로 구현할 수 있었지만, 언제쯤 풀이를 생각해낼 수 있을까...
# 뭐든 꾸준함은 못이긴다고 했던가 화이팅 하자 아자아자!!!