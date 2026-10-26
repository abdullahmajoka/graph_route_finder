
warehouse = {
    "Receiving": {"Aisle1": 40, "Aisle2": 70},
    "Aisle1": {"Aisle2": 30, "Packing Station": 90},
    "Aisle2": {"Packing Station": 35},
    "Packing Station": {}
}

heuristic = {
    "Receiving": 100,
    "Aisle1": 70,
    "Aisle2": 35,
    "Packing Station": 0
}


def get_g(path):
    total = 0

    for i in range(len(path) - 1):
        current_node = path[i]
        next_node = path[i + 1]
        total += warehouse[current_node][next_node]

    return total


def get_f(path):
    last_node = path[-1]
    return get_g(path) + heuristic[last_node]


def a_star(start, goal):
    frontier = [[start]]

    while frontier:
        frontier.sort(key=get_f)
        path = frontier.pop(0)
        node = path[-1]

        print(
            "Exploring:", node,
            "Path:", path,
            "f =", get_f(path)
        )

        if node == goal:
            return path

        for neighbour in warehouse[node]:
            if neighbour not in path:
                new_path = path + [neighbour]
                frontier.append(new_path)

    return None


answer = a_star("Receiving", "Packing Station")

print()
print("Path found by A*:", answer)

if answer is not None:
    print("Total cost of this path:", get_g(answer))
