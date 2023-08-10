# 최대힙, 최소힙 둘다 사용 -> 참고
import heapq
import sys


def get_middle(data):
    left = []
    right = []
    mid = data[0]
    result = [mid]
    for idx, val in enumerate(data[1:]):
        if val > mid:
            heapq.heappush(left, val)
        else:
            heapq.heappush(right, (-val, val))
        if idx % 2 == 1:
            if len(right) < len(left):
                heapq.heappush(right, (-mid, mid))
                mid = heapq.heappop(left)
            elif len(right) > len(left):
                heapq.heappush(left, mid)
                mid = heapq.heappop(right)[1]
            result.append(mid)
    print(len(result))

    for i in range(len(result)):
        if i != 0 and (i + 1) % 10 == 1:
            print()
        print(result[i], end=" ")
    print()


t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    d = []
    m = int(sys.stdin.readline().rstrip())
    if m % 10 == 0:
        for _ in range(m // 10):
            d.extend(list(map(int, sys.stdin.readline().rstrip().split())))
    else:
        for _ in range(m // 10 + 1):
            d.extend(list(map(int, sys.stdin.readline().rstrip().split())))

    get_middle(d)
