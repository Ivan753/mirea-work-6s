"""
Реализация роевого алгоритма для работы
с функциями от двух переменных
"""

import random as r
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.best_x = None
        self.best_y = None


class Swarm:
    def __init__(self, count, x_min, x_max, y_min, y_max):
        self.step = 0
        self.birds = []
        self.c1 = 1
        self.c2 = 0.1

        for _ in range(count):
            self.birds.append(
                Bird(
                    r.randint(x_min, x_max),
                    r.randint(y_min, y_max),
                )
            )

    def go(self):
        self.step += 1

        f = self.f
        c = 1           # инертность
        c1 = self.c1    # коэффициент лучшего вектора агента
        c2 = self.c2    # коэффициент лучгеко ветора стаи

        x = []  # для рендеринга
        y = []  # для рендеринга

        # получаем геометрический центр роя
        swarm_x = 0
        swarm_y = 0
        for bird in self.birds:
            swarm_x += bird.x
            swarm_y += bird.y

        # пересчитываем положения птиц
        for bird in self.birds:
            if bird.best_x:
                bird.x = c + r.random()*(bird.best_x - bird.x)*c1 + r.random()*(swarm_x - bird.x)*c2
                bird.y = c + r.random()*(bird.best_y - bird.y)*c1 + r.random()*(swarm_y - bird.y)*c2
            else:
                bird.best_x = bird.x
                bird.best_y = bird.y
                bird.x = c + r.random() * (swarm_x - bird.x) * c2
                bird.y = c + r.random() * (swarm_y - bird.y) * c2

            if f(bird.x, bird.y) > f(bird.best_x, bird.best_y):
                bird.best_x = bird.x
                bird.best_y = bird.y

            x.append(bird.x)
            y.append(bird.y)

        # возвращаем положения точек
        return x, y

    # искомая функция
    def f(self, x, y):
        return 100*(-(x-50)**2 - (y-100)**2)


if __name__ == '__main__':
    swarm = Swarm(15, -10, 10, -10, 10)

    # отрисовываем
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)

    def animate(i):
        # получаем положения агентов на текущей итерации
        xs, ys = swarm.go()

        ax1.clear()
        plt.ylim(-100, 100)
        plt.xlim(-100, 100)
        ax1.plot(xs, ys, 'ro')

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Положение агентов')

    ani = animation.FuncAnimation(fig, animate, interval=100)
    plt.show()
