
from queue import Queue
from draw_tree import Node, draw_tree
from change_color import change_color

def bfs(tree_root):
    q = Queue()
    q.put(tree_root)
    step = 0

    while not q.empty():
        step += 2
        current_node = q.get()

        if not current_node:
            continue


        current_node.color = change_color(step)
        if current_node.left:
            q.put(current_node.left)
        if current_node.right:
            q.put(current_node.right)

        draw_tree(tree_root)

root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

bfs(root)
