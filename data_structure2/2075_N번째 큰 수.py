import heapq
import sys

n = int(input())
heap = []

for _ in range(n):
    num = map(int, input().split())
    for i in num:
        # 메모리 초과 이슈,,해결 코드
        if len(heap) < n:
            heapq.heappush(heap, i)
        else:
            if heap[0] < i:
                heapq.heappop(heap)
                heapq.heappush(heap, i)

print(heap[0])
