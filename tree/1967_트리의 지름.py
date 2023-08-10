import sys

sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

visited = [-1] * (n + 1)
visited[1] = 0


def dfs(x, w):
    for a, b in graph[x]:
        if visited[a] == -1:
            visited[a] = w + b
            dfs(a, w + b)


dfs(1, 0)

start = visited.index(max(visited))

visited = [-1] * (n + 1)
visited[start] = 0
dfs(start, 0)

print(max(visited))
