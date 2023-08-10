import sys

n = int(input())
arr = list(map(int, input().split()))
num = int(input())


def dfs(v):
    arr[v] = -2  # 범위가 -1< <50
    for i in range(n):
        if v == arr[i]:
            dfs(i)


dfs(num)
cnt = 0

for i in range(n):
    if arr[i] != -2 and i not in arr:
        cnt += 1

print(cnt)
