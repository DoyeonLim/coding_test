# 아이디어 참고
# 1. 시작시간을 오름차순으로 정렬 2. 끝나는 시간을 기준으로 정렬

import sys

input = sys.stdin.readline

n = int(input())

time = []
for _ in range(n):
    start, end = map(int, input().split())
    time.append([start, end])

time = sorted(time, key=lambda a: a[0])  # 시작시간 정렬
time = sorted(time, key=lambda a: a[1])  # 끝나는 시간 정렬

last = 0
cnt = 0

for i, j in time:
    if i >= last:
        cnt += 1
        last = j

print(cnt)
