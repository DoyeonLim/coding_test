import sys
import heapq  # 까먹었던 heapq

n = int(input())
heap = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -num)
