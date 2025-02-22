
from draw_tree import Node, draw_tree
from change_color import change_color

def dfs(tree_root):
    stack = [tree_root]
    step = 0

    while stack:
        step += 2
        current_node = stack.pop()
        if not current_node:
            continue

        current_node.color = change_color(step)

        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)
        
        draw_tree(tree_root)

root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

dfs(root)