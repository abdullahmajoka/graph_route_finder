
campus = {
    "Hostel": {"Cafeteria": 150, "Admin Block": 300},
    "Cafeteria": {"Academic Block": 200},
    "Admin Block": {"Academic Block": 120},
    "Academic Block": {"Library": 100},
    "Library": {}
}

heuristic = {
    "Hostel": 350,
    "Cafeteria": 260,
    "Admin Block": 150,
    "Academic Block": 90,
    "Library": 0
}


def get_h(path):
    return heuristic[path[-1]]


def get_g(path):
    total = 0

    for i in range(len(path) - 1):
        current_node = path[i]
        next_node = path[i + 1]
        total += campus[current_node][next_node]

    return total


def gbfs(start, goal):
    frontier = [[start]]
    visited = []

    while frontier:
        frontier.sort(key=get_h)
        path = frontier.pop(0)
        node = path[-1]

        if node in visited:
            continue

        visited.append(node)

        print(
            "Exploring:", node,
            "Path:", path,
            "h =", get_h(path)
        )

        if node == goal:
            return path

        for neighbour in campus[node]:
            if neighbour not in visited:
                new_path = path + [neighbour]
                frontier.append(new_path)

    return None


answer = gbfs("Hostel", "Library")

print()
print("Path found by GBFS:", answer)

if answer is not None:
    print("Total cost of this path:", get_g(answer))
