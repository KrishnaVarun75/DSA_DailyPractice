def adj(n, m): 
    adj_mat = [[0] * (n + 1) for _ in range(n + 1)]
    for u,v in m:
        adj_mat[u][v]=1
        adj_mat[v][u]=1
    return adj_mat

    

if __name__ == '__main__':
    n = 5   
    m = [(1, 2), (1, 3), (3, 4), (4, 5)]
    result = adj(n, m)
    for row in result[1:]:
        print(row[1:])