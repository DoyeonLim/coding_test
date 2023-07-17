n, k = map(int, input().split())
lis = [i for i in range(1, n + 1)]
num = 0
result = []

for _ in range(n):
    num += k - 1
    if num >= len(lis):
        num = num % len(lis)
    result.append(str(lis[num]))
    lis.pop(num)

print("<", ", ".join(result), ">", sep="")
