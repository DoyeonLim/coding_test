import sys

sys.setrecursionlimit(10**5)

n = int(input())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))

arr = [False] * (n + 1)
for i in range(n):
    arr[inorder[i]] = i


def preorder(inorder_s, inorder_e, postorder_s, postorder_e):
    if (inorder_s > inorder_e) or (postorder_s > postorder_e):
        return
    root = postorder[postorder_e]
    leftNode = arr[root] - inorder_s
    rightNode = inorder_e - arr[root]
    print(root, end=" ")
    preorder(
        inorder_s, inorder_s + leftNode - 1, postorder_s, postorder_s + leftNode - 1
    )
    preorder(
        inorder_e - rightNode + 1, inorder_e, postorder_e - rightNode, postorder_e - 1
    )


preorder(0, n - 1, 0, n - 1)
