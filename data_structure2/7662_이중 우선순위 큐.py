# 최소힙, 최대힙 둘다 구현 -> 참고

import heapq
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    k = int(sys.stdin.readline())
    visitied = [False] * 1000001
    min_heap = []
    max_heap = []

    for i in range(k):
        op, num = sys.stdin.readline().split()
        if op == "I":
            heapq.heappush(min_heap, (int(num), i))
            heapq.heappush(max_heap, (-int(num), i))
            visitied[i] = True
        else:
            if num == "-1":
                while min_heap and not visitied[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visitied[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
            if num == "1":
                while max_heap and not visitied[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visitied[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
    while min_heap and not visitied[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visitied[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if len(min_heap) == 0 or len(max_heap) == 0:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])
