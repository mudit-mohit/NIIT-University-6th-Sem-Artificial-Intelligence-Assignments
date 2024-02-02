def is_valid(state):
    farmer, wolf, goat, cabbage = state
    return not ((wolf == goat and farmer != goat) or (goat == cabbage and farmer != cabbage))
def generate_child_states(current_state, path):
    farmer, wolf, goat, cabbage = current_state
    possible_actions = [
        (not farmer, wolf, goat, cabbage),
        (not farmer, not wolf, goat, cabbage),
        (not farmer, wolf, not goat, cabbage),
        (not farmer, wolf, goat, not cabbage)
    ]
    child_states = [(action, path + [action]) for action in possible_actions if is_valid(action)]
    return child_states
def print_path(path):
    print("Path:")
    for state in path:
        print(tuple(map(int, state)))
def main():
    initial_state = (0, 0, 0, 0)
    goal_state = (1, 1, 1, 1)
    queue = [(initial_state, [initial_state])]
    while queue:
        current_state, path = queue.pop(0)
        if current_state == goal_state:
            print("Goal reached!")
            print_path(path)
            break
    child_states = generate_child_states(current_state, path)
    for child_state, child_path in child_states:
            queue.append((child_state, child_path))
if __name__ == "__main__":
    main()