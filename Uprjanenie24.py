def fix_mst(parent, costs, v, w, c):

    path = []
    x = v

    while x != -1:
        path.append(x)
        x = parent[x]

    x = w
    while x not in path:
        x = parent[x]

    max_cost = 0

    y = v
    while y != x:

        edge = (y, parent[y])

        if costs[edge] > max_cost:
            max_cost = costs[edge]

        y = parent[y]

    y = w
    while y != x:

        edge = (y, parent[y])

        if costs[edge] > max_cost:
            max_cost = costs[edge]

        y = parent[y]

    if c < max_cost:
        print("T is not MST")
        print("Replace largest edge with new edge")
    else:
        print("T is still MST")