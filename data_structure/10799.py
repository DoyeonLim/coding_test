bar = list(input())
res = 0
stack = []

for i in range(len(bar)):
    if bar[i] == "(":
        stack.append("(")
    else:
        if bar[i - 1] == "(":
            stack.pop()
            res += len(stack)
        else:
            stack.pop()
            res += 1

print(res)
