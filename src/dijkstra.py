def dijkstra(start, matrix):
    VERTEX_COUNT = len(matrix)
    visited = [False] * VERTEX_COUNT
    INFINITY = 10 ** 6
    weight = [INFINITY] * VERTEX_COUNT
    weight[start] = 0

    for _ in range(VERTEX_COUNT):
        min_weight = INFINITY
        min_vertex = -1

        for i in range(VERTEX_COUNT):
            if not visited[i] and min_weight > weight[i]:
                min_vertex = i
                min_weight = weight[i]

        for i in range(VERTEX_COUNT):
            current_vertex_weight = matrix[min_vertex][i]

            if current_vertex_weight < weight[i]:
                weight[i] = current_vertex_weight

        visited[min_vertex] = True

    return weight
