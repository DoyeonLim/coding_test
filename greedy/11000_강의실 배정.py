import sys
import heapq

input = sys.stdin.readline

n = int(input())
time = []
room = []
for _ in range(n):
    s, t = map(int, input().split())
    time.append([s, t])

time = sorted(time, key=lambda a: a[0])
heapq.heappush(room, time[0][1])

for i in range(1, n):
    if time[i][0] < room[0]:
        heapq.heappush(room, time[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, time[i][1])

print(len(room))
