import sys

input = sys.stdin.readline

n = int(input())
road = list(map(int, input().split()))
money = list(map(int, input().split()))
min_money = money[0]
total = 0

for i in range(len(road)):
    if min_money > money[i]:
        min_money = money[i]
    total += min_money * road[i]  # 참고 코드

print(total)
