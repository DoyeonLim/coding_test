n = int(input())
numbers = list(map(int, input().split()))
tree = [[] for _ in range(n)]


def solution(lis, i):
    mid = len(lis) // 2
    tree[i].append(lis[mid])
    if len(lis) == 1:
        return
    solution(lis[:mid], i + 1)
    solution(lis[mid + 1 :], i + 1)


solution(numbers, 0)

for i in range(n):
    print(*tree[i])
