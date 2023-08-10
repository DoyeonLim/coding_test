import sys

input = sys.stdin.readline

n = int(input())
time = list(map(int, input().split()))
time.sort()
total = 0

for t in range(len(time)):
    sum_time = sum(time[: t + 1])
    total = total + sum_time

print(total)
