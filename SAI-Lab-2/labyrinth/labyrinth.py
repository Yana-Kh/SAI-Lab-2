from collections import deque


def shortest_path(maze, start, goal):
    rows, cols = len(maze), len(maze[0])

    # Проверка на границы и доступность начальной и конечной точки
    if maze[start[0]][start[1]] == 0 or maze[goal[0]][goal[1]] == 0:
        return -1

    # Вспомогательные структуры: очередь и множество посещённых клеток
    queue = deque([(start[0], start[1], 0)])  # (x, y, шаги)
    visited = set()
    visited.add((start[0], start[1]))

    # Возможные направления движения: вверх, вниз, влево, вправо
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Алгоритм BFS
    while queue:
        x, y, steps = queue.popleft()

        # Проверка на достижение цели
        if (x, y) == goal:
            return steps

        # Проход по всем возможным направлениям
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Проверка границ и доступности следующей клетки
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 1 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))

    # Если цель недостижима
    return -1


# Пример использования
maze = [
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 1, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
    [0, 1, 0, 1, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 0, 0, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 0, 0, 1, 0, 1, 1, 1],
]

# Начальная и целевая точка
initial = (0, 0)  # Стартовая позиция (верхний левый угол)
goal = (9, 9)     # Целевая позиция (правый нижний угол)

# Запуск функции и вывод результата
result = shortest_path(maze, initial, goal)
print(f"Кратчайший путь: {result if result != -1 else 'Путь недостижим'}")
