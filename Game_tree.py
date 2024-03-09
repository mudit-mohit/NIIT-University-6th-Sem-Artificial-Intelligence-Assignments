import random
class Node:
    def __init__(self, utility=None, children=None):
        self.utility = utility
        self.children = children if children else []
def generate_game_tree(depth):
    if depth == 0:
        return Node(utility=random.uniform(-5, 5))
    else:
        num_children = random.randint(3, 5)
        children = [generate_game_tree(depth - 1) for _ in range(num_children)]
        return Node(children=children)
def minmax(node, depth, maximizing_player, num_nodes_visited=0):
    if depth == 0 or not node.children:
        return node.utility, num_nodes_visited+1
    if maximizing_player:
        value = -float('inf')
        for child in node.children:
            child_value, num_child_nodes_visited = minmax(child, depth-1, False, num_nodes_visited+1)
            value = max(value, child_value)
        return value, num_nodes_visited+1
    else:
        value = float('inf')
        for child in node.children:
            child_value, num_child_nodes_visited = minmax(child, depth-1, True, num_nodes_visited+1)
            value = min(value, child_value)
        return value, num_nodes_visited+1
def minmax_with_alpha_beta_pruning(node, depth, maximizing_player, alpha=-float('inf'), beta=float('inf'), num_nodes_visited=0):
    if depth == 0 or not node.children:
        return node.utility, num_nodes_visited+1
    if maximizing_player:
        value = -float('inf')
        for child in node.children:
            child_value, num_child_nodes_visited = minmax_with_alpha_beta_pruning(child, depth-1, False, alpha, beta, num_nodes_visited+1)
            value = max(value, child_value)
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value, num_nodes_visited+len(node.children)
    else:
        value = float('inf')
        for child in node.children:
            child_value, num_child_nodes_visited = minmax_with_alpha_beta_pruning(child, depth-1, True, alpha, beta, num_nodes_visited+1)
            value = min(value, child_value)
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value, num_nodes_visited + len(node.children)   

def count_nodes(node):
    if not node.children:
        return 1
    else:
        count = 1
        for child in node.children:
            count += count_nodes(child)
        return count

def main():
    depth = 5
    root_node = generate_game_tree(depth)
    
    total_nodes = count_nodes(root_node)
    print(f"Total number of nodes in the game tree: {total_nodes}")

    print("MINMAX without alpha-beta pruning:")
    utility, num_nodes_visited = minmax(root_node, depth, True)
    print(f"Best choice: {utility}")
    print(f"Number of nodes visited: {num_nodes_visited}")

    print("MINMAX with alpha-beta pruning:")
    utility, num_nodes_visited = minmax_with_alpha_beta_pruning(root_node, depth, True)
    print(f"Best choice: {utility}")
    print(f"Number of nodes visited: {num_nodes_visited}")

if __name__ == "__main__":
    main()
