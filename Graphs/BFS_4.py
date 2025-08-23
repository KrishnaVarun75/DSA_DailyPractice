from collections import deque

def bfs(n,m):
    result = []
    visited = [False]*n
    q = deque()
    q.append(0)
    visited[0] = True

    while q:
        node = q.popleft()
        result.append(node)
        for neigh in m[node]:
            if not visited[neigh]:
                visited[neigh] = True
                q.append(neigh)
    return result

if __name__ == '__main__':
    n =5
    m =  [[2, 3, 1], [0], [0, 4], [0], [2]]
    print(bfs(n,m))





