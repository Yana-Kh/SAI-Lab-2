from collections import deque

# Вспомогательная функция для BFS
def bfs(r, c, visited, rows, cols):
    queue = deque([(r, c)])
    visited[r][c] = True

    # Все возможные направления движения (включая диагонали)
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),  # вверх, вниз, влево, вправо
        (-1, -1), (-1, 1), (1, -1), (1, 1)  # диагонали
    ]

    while queue:
        x, y = queue.popleft()

        # Проверяем все соседние клетки
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Условие: внутри границ, это земля (1), и ещё не посещено
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

def num_islands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    islands_count = 0


    # Основной цикл для перебора всех клеток матрицы
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and not visited[i][j]:
                # Запускаем BFS для нового острова
                bfs(i, j, visited, rows, cols)
                islands_count += 1

    return islands_count

# Пример использования
grid = [
    [0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1]
]

print("Общее количество островов:", num_islands(grid))
