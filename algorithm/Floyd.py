

adj_matrix = [
[0, 2, 65535, 65535, 3],
[65535, 0, 1, 3, -1],
[4, 65535, 0, 1, 65535],
[65535, 65535, 65535, 0, 1],
[65535, 2, 4, 65535, 0],
]

def floyd(adj_matrix, n):
    distances = [[0 for i in range(0, n)] for j in range(0, n)]
    path = [[0 for i in range(0, n)] for j in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            distances[i][j] = adj_matrix[i][j]

    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
                    path[i][j] = k
    return distances, path

res, path = floyd(adj_matrix, len(adj_matrix))
for i in range(len(res)):
    print(res[i])

print()
for i in range(len(path)):
    print(path[i])



