import sys
import heapq

max_heap = []
min_heap = []

n = int(sys.stdin.readline())
for _ in range(n):
    p, l = map(int, sys.stdin.readline().split())
    heapq.heappush(min_heap, (l, p))
    heapq.heappush(max_heap, (-l, -p))

m = int(sys.stdin.readline())
for _ in range(m):
    order = list(map(str, sys.stdin.readline().split()))
    if order[0] == "recommend":
        if int(order[1]) == 1:
            print(max_heap[0][1] * -1)
        else:
            print(min_heap[0][1])
    elif order[0] == "add":
        heapq.heappush(min_heap, (int(order[2]), int(order[1])))
        heapq.heappush(max_heap, (-1 * int(order[2]), -1 * int(order[1])))
    elif order[0] == "sovled":
        if int(order[1]) == (max_heap[0][1] * -1):
            heapq.heappop(max_heap)
        elif int(order[1]) == min_heap[0][1]:
            heapq.heappop(min_heap)
