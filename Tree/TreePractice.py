from collections import deque

tree = ["A", "B", "C", "D", "E", "F", None, "G"]

n = len(tree)

def preorder(tree, i):
    if i < len(tree):
        print(tree[i], end=" ") # 방문 처리(출력)
        left, right = 2*i + 1, 2*i + 2

        if left < len(tree) and tree[left] is not None:
            preorder(tree,left)
        if right < len(tree) and tree[right] is not None:
            preorder(tree,right)

def inorder(tree, i):
    if i < len(tree):
        left, right = 2*i + 1, 2*i + 2

        if left < len(tree) and tree[left] is not None:
            inorder(tree,left)

        print(tree[i], end=" ") # 방문 처리(출력)
        
        if right < len(tree) and tree[right] is not None:
            inorder(tree,right)

def postorder(tree, i):
    if i < len(tree):
        left, right = 2*i + 1, 2*i + 2

        if left < len(tree) and tree[left] is not None:
            postorder(tree,left)
        
        if right < len(tree) and tree[right] is not None:
            postorder(tree,right)

        print(tree[i], end=" ") # 방문 처리(출력)

def levelorder(tree):
    if not tree:
        return
    
    queue = deque([0])

    while queue:
        parent = queue.popleft()
        
        print(tree[parent], end=" ")

        left, right = 2*parent + 1, 2*parent + 2

        if left < len(tree) and tree[left] is not None:
            queue.append(left)
        if right < len(tree) and tree[right] is not None:
            queue.append(right)


# 부모 노드 구하기
for i in range(n-1,0,-1):
    if tree[i]:
        print(f"Parent of {tree[i]} -> {tree[(i-1)//2]}")

# 자식 노드 구하기
for i in range(n):
    if tree[i]:
        print(f"Parent: {tree[i]}", end = ", ")
        left, right = 2*i + 1, 2*i + 2

        if left < n and tree[left] is not None:
            print(f"Left: {tree[left]}",end = ", ")
        if right < n and tree[right] is not None:
            print(f"Right: {tree[right]}",end=" ")
        print()

preorder(tree,0) # A B D G E C F
print()
inorder(tree,0) # G D B E A F C
print()
postorder(tree,0) # G D E B F C A
print()
levelorder(tree) # A B C D E F G