from collections import deque

def water_jug_bfs(initial, goal, sizes):
    # Инициализируем очередь и множество для отслеживания посещённых состояний
    queue = deque([(initial, [], [initial])])  # (текущее состояние, действия, список состояний)
    visited = set()
    visited.add(initial)

    while queue:
        state, actions, path = queue.popleft()

        # Проверка, достигнута ли цель
        if goal in state:
            print("Все состояния на пути к решению:")
            for step, s in enumerate(path):
                print(f"Шаг {step}: {s}")
            print("\nПоследовательность действий:", actions)
            return  # Останавливаемся после первого найденного решения

        # Проходим по всем возможным действиям
        for i in range(len(sizes)):
            # 1. Наполнить i-й кувшин до верха
            new_state = list(state)
            new_state[i] = sizes[i]
            if tuple(new_state) not in visited:
                visited.add(tuple(new_state))
                queue.append((tuple(new_state), actions + [('Fill', i)], path + [tuple(new_state)]))

            # 2. Опустошить i-й кувшин
            new_state = list(state)
            new_state[i] = 0
            if tuple(new_state) not in visited:
                visited.add(tuple(new_state))
                queue.append((tuple(new_state), actions + [('Dump', i)], path + [tuple(new_state)]))

            # 3. Перелить из i-го в j-й кувшин
            for j in range(len(sizes)):
                if i != j:  # Переливаем только между разными кувшинами
                    new_state = list(state)
                    transfer = min(state[i], sizes[j] - state[j])  # Максимально возможный объём перелива
                    new_state[i] -= transfer
                    new_state[j] += transfer
                    if tuple(new_state) not in visited:
                        visited.add(tuple(new_state))
                        queue.append((tuple(new_state), actions + [('Pour', i, j)], path + [tuple(new_state)]))

    print("Решение не найдено")

# Исходные данные
initial = (1, 3, 2)
goal = 10
sizes = (5, 11, 21)

# Запуск функции
water_jug_bfs(initial, goal, sizes)
