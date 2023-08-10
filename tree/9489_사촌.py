# 아이디어 코드 참고

import sys

while True:
    n, k = map(int, sys.stdin.readline().rstrip().split())

    if n == 0 and k == 0:
        break

    a = [-1] + list(map(int, sys.stdin.readline().rstrip().split()))
    parent = [False] * (n + 1)
    parent[0] = -1
    target = 0
    idx = -1

    for i in range(1, n + 1):
        if a[i] == k:
            target = i
        if a[i] != a[i - 1] + 1:
            idx += 1
        parent[i] = idx

    ans = 0
    for i in range(1, n + 1):
        if parent[i] != parent[target] and parent[parent[i]] == parent[parent[target]]:
            ans += 1

    print(ans)
