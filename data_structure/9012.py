n = int(input())

for i in range(n):
    tmp = 0
    s = list(input())
    length = len(s)
    for j in range(length):
        if s[j] == "(":
            tmp = tmp + 1
        else:
            tmp = tmp - 1
        if tmp < 0:
            print("NO")
            break
    if tmp == 0:
        print("YES")
    elif tmp > 0:
        print("NO")
