# 참고한 코드
from collections import deque

n = int(input())
balloon = deque(enumerate(map(int, input().split()), 1))
ans = []
index = 0

while balloon:
    if index > 0:
        a, b = balloon.popleft()
        balloon.append((a, b))
        index -= 1
    elif index < 0:
        a, b = balloon.pop()
        balloon.appendleft((a, b))
        index += 1
    else:
        a, b = balloon.popleft()
        ans.append(a)
        if b > 0:
            index = b - 1
        else:
            index = b
print(*ans)
