import sys

n, m = map(int, sys.stdin.readline().split())
dict = {}
idx = 1

for _ in range(n):
    s = sys.stdin.readline().rstrip()
    dict[idx] = s  # dictionary 2개 만들기
    dict[s] = idx
    idx += 1

for _ in range(m):
    q = sys.stdin.readline().rstrip()
    if q.isalpha():
        print(dict[q])
    elif q.isdigit():
        print(dict[int(q)])
