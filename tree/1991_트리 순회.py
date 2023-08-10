import sys

n = int(sys.stdin.readline())

tree = {}

for i in range(n):  # 입력값 root, left, right에 저장
    root, left, right = sys.stdin.readline().split()
    tree[root] = [left, right]


def preorder(root):  # preorder(root -> left -> right)
    if root != ".":
        print(root, end="")
        preorder(tree[root][0])
        preorder(tree[root][1])


def inorder(root):  # inorder(left -> root -> right)
    if root != ".":
        inorder(tree[root][0])
        print(root, end="")
        inorder(tree[root][1])


def postorder(root):  # postorder(left -> right -> root)
    if root != ".":
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end="")


preorder("A")
print()
inorder("A")
print()
postorder("A")
