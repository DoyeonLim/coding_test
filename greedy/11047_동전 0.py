import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
coin.sort(reverse=True)
cnt = 0

for i in coin:
    if i > k:
        pass
    else:
        cnt = cnt + k // i  # 몫
        k = k % i  # 나머지
        if k == 0:
            break

print(cnt)
