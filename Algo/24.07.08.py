# 엘리스 코딩경진대회 1회차 목표량

from itertools import permutations

ins = input()
tmp = list(ins.strip())
today = [int(i) for i in tmp]


comb = []

for i in permutations(today, len(today)):
    comb.append(int(''.join(map(str, i))))

comb.sort()
for i in range(len(comb)):
    if comb[i-1] == int(ins) and comb[i-1] != comb[i]:
        print(comb[i])
        
# permutations 라는 내장라이브러리를 사용하여 조합을 만들고 조합을 이용해서 구현
# 112, 999같은 엣지 케이스들이 있었으나 999같이 조합이 모두 같은 수는 엣지케이스로 안넣은것같다.
# 해당 조건들을 다 생각해주어야하고, join을 적절히 사용해서 용이하게 가공했다.