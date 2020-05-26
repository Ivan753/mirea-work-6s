"""
Реализация алгоритма пчелиной колонии для случая поиска максимума
функции от двух переменных

Краткое описание алгоритма:
- на каждой итерации рассчитывается две области, которые характеризуются центрами областей
- в каждую область посылается по 5 пчел, значения найденных точек формируют новые две области
- и так далее, пока не произайдет стогнация на одной области
"""

import math
import random as r
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Bee:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Swarm:
    def __init__(self, S, D, C, N, M, init_state):
        self.step = 0
        self.bees = []  # список пчел
        self.S = S      # количество пчел
        self.D = D      # диаметр областей
        self.C = C      # расстояние между точками, меньше которого считать одной областью
        self.N = N      # количество пчел, посылаемых в лучшую область
        self.M = M      # количество пчел, посылаемых в область с потенциалом
        self.v = [      # начальное положение областей
            {'x': init_state['x'], 'y': init_state['y']},
            {'x': init_state['x'], 'y': init_state['y']}
        ]

        for _ in range(self.S):
            self.bees.append(
                Bee(
                    init_state['x'],
                    init_state['y'],
                )
            )

    def go(self):
        self.step += 1
        bees = self.bees
        N = self.N
        M = self.M
        v = self.v
        D = self.D

        # направляем пчел на исследование участков
        k = 0
        for i in range(N):
            bees[k].x = r.randint(v[0]['x'] - D/2, v[0]['x'] + D/2)
            bees[k].y = r.randint(v[0]['y'] - D/2, v[0]['y'] + D/2)
            k += 1

        for i in range(M):
            bees[k].x = r.randint(v[1]['x'] - D/2, v[1]['x'] + D/2)
            bees[k].y = r.randint(v[1]['y'] - D/2, v[1]['y'] + D/2)
            k += 1

        # сортируем найденные точки по значению целевой функции
        mass = []
        link = {}
        k = 0
        for bee in bees:
            val = self.f(bee.x, bee.y)
            mass.append(val)
            link[val] = k
            k += 1

        mass.sort(reverse=True)

        # выполняем формирование зон
        # первая зона формируется вокруг точки с наибольшем значением целевой функции на этапе
        v[0] = {
            'x': bees[link[mass[0]]].x,
            'y': bees[link[mass[0]]].y,
        }

        # вторая зона формируется вокруг точки, которая первая будет удалена от центра
        # первой зоны на достаточное расстояние
        for item in mass[1:]:
            if not self.close(v[0], {'x': bees[link[item]].x, 'y': bees[link[item]].y}):
                v[1] = {
                    'x': bees[link[item]].x,
                    'y': bees[link[item]].y,
                }
                break

        # возвращаем положения областей и максимальное здачение
        self.v = v
        return v, mass[0]

    # подсчет расстояния
    def close(self, a, b):
        if math.sqrt((a['x'] - b['x']) ** 2 + (a['y'] - b['y']) ** 2) < self.C:
            return True
        return False

    # искомая функция
    def f(self, x, y):
        return 100*(-(x-50)**2 - (y-100)**2)


if __name__ == '__main__':
    swarm = Swarm(10, 10, 10, 5, 5, {'x': 0, 'y': 0})

    # визуализация
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)

    def animate(i):
        # получаем положения агентов на текущей итерации
        v, max = swarm.go()

        ax1.clear()
        plt.ylim(-200, 200)
        plt.xlim(-200, 200)

        X = [
            v[0]['x'],
            v[1]['x'],
        ]
        Y = [
            v[0]['y'],
            v[1]['y'],
        ]

        ax1.plot(X, Y, 'ro')

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Положение агентов')

    ani = animation.FuncAnimation(fig, animate, interval=100)
    plt.show()
