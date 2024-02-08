from collections import deque

def bfs(graph, initial, goal):
    queue = deque([[initial]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        print("Queue:", queue)
        print("Total nodes in queue:", sum(len(p) for p in queue))
        print("Current path:", path)

        if node == goal:
            print("Goal reached! Optimal path:", path)
            return

        if node not in visited:
            for successor in get_successors(graph, node):
                new_path = list(path)
                new_path.append(successor)
                queue.append(new_path)

            visited.add(node)

def get_successors(graph, node):
    return [i for i, connected in enumerate(graph[node]) if connected == 1]

# Example usage:
# Replace the 'graph' matrix, 'initial_node', and 'goal_node' with your specific values
graph = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 1, 1],
    [0, 1, 1, 0, 1],
    [0, 0, 1, 1, 0]
]

initial_node = 0
goal_node = 4

bfs(graph, initial_node, goal_node)
