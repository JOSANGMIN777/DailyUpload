# 10845 큐 실버4

def push(x):
    queue.append(x)

def pop():
    if queue:
        ans = queue.pop(0)
        print(ans)
    else:
        print(-1)

def size():
    print(len(queue))

def empty():
    if len(queue) == 0:
        print(1)
    else:
        print(0)

def front():
    if queue:
        print(queue[0])
    else:
        print(-1)

def back():
    if queue:
        print(queue[-1])
    else:
        print(-1)


N = int(input())
orders = []
queue = []
for i in range(N):
    orders.append(input().split())

for order in orders:
    if order[0] == 'push':
        push(order[1])

    elif order[0] == 'front':
        front()

    elif order[0] == 'back':
        back()

    elif order[0] == 'size':
        size()

    elif order[0] == 'pop':
        pop()

    elif order[0] == 'empty':
        empty()