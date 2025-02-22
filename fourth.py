import heapq
from draw_tree import Node, draw_tree

def heap_tree(heap):
    nodes = [Node(val) for val in heap]
    for i in range(len(nodes) // 2):
        if 2 * i + 1 < len(nodes):
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < len(nodes):
            nodes[i].right = nodes[2 * i + 2]
    return nodes[0]

def visualize_heap(heap):
    if not heap:
        print("Heap is empty")
        return
    tree_root = heap_tree(heap)
    draw_tree(tree_root)

heap = []
values = [3, 1, 6, 5, 2, 8, 7, 4]
for value in values:
    heapq.heappush(heap, value)

visualize_heap(heap)
