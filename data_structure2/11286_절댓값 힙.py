import sys
import heapq

n = int(input())
q = []

for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    if num != 0:
        heapq.heappush(q, (abs(num), num))  # heapq에 2개 넣기
    else:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q)[1])
