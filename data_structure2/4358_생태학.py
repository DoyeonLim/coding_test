import sys

dic = dict()
total = 0

while True:
    name = sys.stdin.readline().rstrip()
    if name == "":
        break
    total += 1
    if name in dic:
        n = dic[name]
        n += 1
        dic[name] = n
    else:
        dic[name] = 1

dict_sorted = dict(sorted(dic.items()))

for d in dict_sorted:
    a = dict_sorted[d]
    percent = a / total * 100
    print("%s %.4f" % (d, percent))
