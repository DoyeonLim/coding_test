# 문제 이해 어려움
n = int(input())
cnt = 1
flag = True
stack = []
op = []

for _ in range(n):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        op.append("+")
        cnt += 1

    if stack[-1] == num:
        stack.pop()
        op.append("-")
    else:
        flag = False
        break

if flag == False:
    print("NO")
else:
    for i in op:
        print(i)
