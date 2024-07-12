import sys
input = sys.stdin.readline

result = 0

def sol(n,x,y):
    global result
    if x == r and y == c:
        print(int(result))
        return

    if not (x <= r < x+n and y <= c < y+n): # 각 사분면의 시작부터 끝 범위이다. for문 범위마냥 시작이상 끝미만
        result += n*n
        return

    sol(n/2, x, y)
    sol(n/2, x, y + n/2)
    sol(n/2, x + n/2, y)
    sol(n/2, x + n/2, y + n/2)


N,r,c = map(int,input().split())
sol(1 << N, 0, 0)

# 이건 뭐 거의 보고 푼 거라 푼거같지가 않다
# 하지만, but, however 모르는 내용을 그냥 풀어재낄만큼 내가 천재가 아니라
# 공부하는 시간이 필요했다. 앞으로 분할정복 나오면 다 풀어버리겠다.
# 큰 바둑판 배열을 1,2,3,4분면으로 쪼개어 들어가면서 값을 찾는다. 
# 덕분에 메모리를 상당히 아낄 수 있다.
