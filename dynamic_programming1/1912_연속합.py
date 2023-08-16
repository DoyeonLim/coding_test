import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
sum_val = [numbers[0]]

for i in range(0, n - 1):
    sum_val.append(max(sum_val[i] + numbers[i + 1], numbers[i + 1]))

print(max(sum_val))
