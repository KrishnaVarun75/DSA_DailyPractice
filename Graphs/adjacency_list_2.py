def adj(n,m):
    adj_list = [[] for _ in range(n+1)]
    for u , v in m:
        adj_list[u].append(v)
        adj_list[v].append(u)
    return adj_list

if __name__ == '__main__':
    n = 5   
    m = [(1, 2), (1, 3), (3, 4), (4, 5)]
    result = adj(n, m)
    for i in range(1,n+1):
        print(f'{i}:{result[i]}')

