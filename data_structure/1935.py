n = int(input())
s = list(input())
stack = []
alpha = []

for _ in range(n):
    alpha.append(int(input()))

for i in s:
    if i.isalpha():
        stack.append(alpha[ord(i) - ord("A")])  # 참고
    else:
        a = stack.pop()
        b = stack.pop()
        if i == "+":
            stack.append(b + a)
        elif i == "-":
            stack.append(b - a)
        elif i == "*":
            stack.append(b * a)
        elif i == "/":
            stack.append(b / a)

print("%.2f" % stack[0])
