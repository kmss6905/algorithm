class Node:
    def __init__(self, value = '', left = None, right = None):
        self.value = value
        self.right = right
        self.left = left

root = Node(value = 'A')
root.left = Node(value = 'B')
root.right = Node(value = 'C')
root.right.right = Node(value = 'F')
root.left.left = Node(value = 'D')
root.left.right = Node(value = 'E')

"""
너비우선탐색
root 노드 부터 가장 가깝게 있는 노드 부터 탐색함.
"""
from collections import deque
def bfs(root):
    visited = []
    if root is None:
        return
    
    # 방문 할 예정인 노드들은 q 에 집어 넣는다.
    q = deque()
    
    # root 부터 시작하기 때문에 root 먼저 q 에 넣는다.
    q.append(root)
    while q:
        cur_node = q.popleft()
        visited.append(cur_node.value)
        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)
    return visited

print(bfs(root))

"""
깊이우선탐색 - DFS(말 그대로 깊게 먼저 탐색함)
이때 노드를 언제 방문할 것인지에 따라 전위 순회 (Preorder), 중위 순회 (Inorder), 후위 순회 (Postorder) 로 나눌 수 있다

각자의 노드에게 일을 맡기면 된다.
"""

# 전위 순회
def pre_dfs(cur_node):
    if cur_node is None:
        return
    
    print(cur_node.value) # preorder 다음 노드 방문하기 전에 먼저 자기 자신을 방문(여기서는 콘솔로 해당 노드 값 찍기)
    pre_dfs(cur_node.left) # 각자의 노드에게 일을 맡긴다
    pre_dfs(cur_node.right) # 각자의 노드에게 일을 맡긴다

# 중위 순회
def inorder_dfs(cur_node):
    if cur_node is None:
        return

    inorder_dfs(cur_node.left)
    print(cur_node.value)
    inorder_dfs(cur_node.right)


    
# 중위 순회
def post_dfs(cur_node):
    if cur_node is None:
        return

    post_dfs(cur_node.left)
    post_dfs(cur_node.right)
    print(cur_node.value)
