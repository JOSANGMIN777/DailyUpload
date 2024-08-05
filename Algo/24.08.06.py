# 백준 1110 더하기 사이클 브론즈1

N = input()

if int(N) < 10:
    N = '0'+ N

goal = int(N[0])+int(N[1])
new = N[1]+str(goal)[-1]
cnt = 1
while new != N:
    goal = int(new[0])+int(new[1])

    new = new[1] + str(goal)[-1]
    cnt += 1

print(cnt)

# 심심풀이로 브론즈 문제나 풀어볼까 하고 사람들이 많이 푼걸로 시도했는데
# 생각보다 난이도가 있었음
# 뭔가 될듯 안되고 무한루프도는... 이게 진지하게 안풀어서 그런거같은데
# 시키는대로 안하고 자꾸 이상하게 대충 하다가 오래걸린듯