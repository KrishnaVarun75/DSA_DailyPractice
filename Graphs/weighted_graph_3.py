def wg(n, edges, wts, directed=False):
 
    adj_matrix = [[0] * (n + 1) for _ in range(n + 1)]
    adj_list = [[] for _ in range(n + 1)]

    for (u, v), w in zip(edges, wts):
        adj_matrix[u][v] = w
        adj_list[u].append((v, w))

        if not directed: 
            adj_matrix[v][u] = w
            adj_list[v].append((u, w))

    return adj_matrix, adj_list


if __name__ == '__main__':
    n = 5
    edges = [(1, 2), (1, 3), (3, 4), (4, 5)]
    wts   = [2, 4, 7, 1]   

    adj_matrix, adj_list = wg(n, edges, wts, directed=False)

    print("Adjacency Matrix:")
    for row in adj_matrix[1:]:
        print(row[1:])   

    print("\nAdjacency List:")
    for i in range(1, n+1):
        print(f"{i}: {adj_list[i]}")

