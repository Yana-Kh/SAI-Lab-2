import time
from collections import defaultdict
from Problem import Problem
from Node import Node, failure, path_states, expand
from Queue import PriorityQueue, FIFOQueue


# Список городов и расстояний между ними (без повторов)
distances = {
    ('Красный Маныч', 'Новокучерлинский'): 11.8,
    ('Красный Маныч', 'Сабан-Антуста'): 10.9,
    ('Красный Маныч', 'Голубиный'): 2.3,
    ('Красный Маныч', 'Каменная Балка'): 13.8,
    ('Новокучерлинский', 'Ясный'): 20.3,
    ('Сабан-Антуста', 'Каменная Балка'): 15.3,
    ('Сабан-Антуста', 'Кендже-Кулак'): 7.1,
    ('Голубиный', 'Каменная Балка'): 11.1,
    ('Кендже-Кулак', 'Шарахалсун'): 12.9,
    ('Шарахалсун', 'Кучерла'): 7.2,
    ('Кучерла', 'Мирное'): 14.9,
    ('Кучерла', 'Таврический'): 13.2,
    ('Куликовы Копани', 'Маштак-Кулак'): 14.9,
    ('Маштак-Кулак', 'Летняя Ставка'): 9.0,
    ('Летняя Ставка', 'Ясный'): 26.1,
    ('Летняя Ставка', 'Овощи'): 10.2,
    ('Чур', 'Овощи'): 12.8,
    ('Овощи', 'Горный'): 21.9,
    ('Камбулат', 'Малые Ягуры'): 9.8,
    ('Малые Ягуры', 'Казгулак'): 19.3,
    ('Казгулак', 'Ясный'): 40.9,
}


# Задача коммивояжера
class TSP(Problem):
    def __init__(self, start, finish):
        super().__init__(initial=start, goal=finish)
        self.graph = self.build_graph()

    def build_graph(self):
        graph = defaultdict(list)
        for (city1, city2), dist in distances.items():
            graph[city1].append((city2, dist))
            graph[city2].append((city1, dist))
        return graph

    def actions(self, state):
        return self.graph[state]

    def result(self, state, action):
        return action[0]

    def action_cost(self, state, action, result):
        return action[1]

# Функция для поиска решения задачи коммивояжера
def search_TSP(problem):
    border = PriorityQueue([Node(problem.initial)])  # Очередь с приоритетом
    path = set()

    while border:
        node = border.pop()
        if problem.is_goal(node.state):
            return path_states(node), node.path_cost

        path.add(node.state)

        for city, cost in problem.actions(node.state):
            child = Node(city, node, path_cost=node.path_cost + cost)
            if child.state not in path:
                border.add(child)

    return failure


# Реализация поиска в ширину
def breadth_first_search(problem):
    node = Node(problem.initial)
    if problem.is_goal(problem.initial):
        return node
    frontier = FIFOQueue([node])
    reached = {problem.initial}
    while frontier:
        node = frontier.pop()
        for child in expand(problem, node):
            s = child.state
            if problem.is_goal(s):
                return child
            if s not in reached:
                reached.add(s)
                frontier.appendleft(child)
    return failure

# Запуск поиска и замер времени
def run_search(problem, search_fn):
    start_time = time.time()
    result = search_fn(problem)
    end_time = time.time()

    if result != failure:
        route = path_states(result)
        print(f"Маршрут: {' -> '.join(route)}")
        print(f"Общее расстояние: {result.path_cost} км")
    else:
        print("Маршрут не найден.")

    print(f"Время выполнения: {end_time - start_time:.4f} секунд")

# Инициализация задачи
problem = TSP('Красный Маныч', 'Чур')

# Выбор поиска: BFS или поиск с приоритетами (A*)
print("Результат BFS:")
run_search(problem, breadth_first_search)
