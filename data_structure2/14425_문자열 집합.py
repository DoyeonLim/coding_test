import sys

n, m = map(int, input().split())
dict = {}
cnt = 0

for i in range(n):
    s = sys.stdin.readline().rstrip()
    dict[s] = i

for _ in range(m):
    word = sys.stdin.readline().rstrip()
    if word in dict:
        cnt += 1

print(cnt)
