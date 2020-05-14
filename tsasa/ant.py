import random as r


class Ant:
    def __init__(self):
        self.taby = [0, ]
        self.current = 0
        self.finished = False


class Ants:
    def __init__(self, g, a, b, p):
        self.step = 0
        self.ants = []
        self.g = g
        self.a = a
        self.b = b
        self.p = p
        self.countFinished = 0
        self.epoch = 0
        self.t = []

        for _ in range(3):
            self.ants.append(
                Ant()
            )

        for i in range(len(g)):
            self.t.append([0 for _ in range(len(g))])

    def go(self):
        self.step += 1
        g = self.g
        a = self.a
        b = self.b
        p = self.p
        t = self.t  # количество фермента
        _t = t
        q = 1000      # количество фермента на путь

        k = 0
        # считаемт положения муравьев
        for ant in self.ants:

            if ant.finished:
                continue
            variants = g[ant.current]

            P = []
            i = 0

            if len(ant.taby) >= len(g):
                ant.taby.pop(0)
                ant.finished = True
                self.countFinished += 1

            # подсчитывает общую вероятность
            sumP = 0
            for item in variants:
                if item == 0 or i in ant.taby:
                    pass
                else:
                    sumP += t[ant.current][i]**a + 1 / (item**b)
                i += 1

            # подсчитываем вероятность для каждого перехода
            i = 0
            for item in variants:
                if item == 0 or i in ant.taby:
                    P.append(0)
                else:
                    P.append(t[ant.current][i]**a + 1 / (item**b) / sumP)
                i += 1

            if self.step == 1 and self.epoch == 0:
                P = [0 for _ in range(len(g))]
                P[k+1] = 1

            # выбираем переход
            ant_old = ant.current
            choice = r.choices([i for i in range(len(g))], weights=P)
            ant.current = choice[0]
            ant.taby.append(ant.current)
            # считаем фермент
            # сколько фермента осталось
            dt = q / g[ant_old][ant.current]
            # испарение для всех
            for i in range(len(_t)):
                for j in range(len(_t[i])):
                    _t[i][j] = _t[i][j] * (1 - p)
            # новое количество фермента
            _t[ant_old][ant.current] = dt + _t[ant_old][ant.current] * p

        self.t = _t

        if self.step > 20:
            self.epoch = 1000000000
        if self.countFinished >= len(self.ants):
            self.countFinished = 0
            self.epoch += 1
            self.step = 0
            k = 0
            for ant in self.ants:
                ant.taby = [ant.current]
                ant.finished = False

        return self.epoch


if __name__ == '__main__':
    graph = [
        [0, 20, 42, 35],
        [20, 0, 30, 34],
        [42, 30, 0, 12],
        [35, 34, 12, 0],
    ]
    ants = Ants(graph, 1, 1, 0.7)

    while (ants.go() < 100000):
        pass

    for i in range(len(ants.t)):
        print()
        for j in range(len(ants.t[i])):
            print(0 if ants.t[i][j] < 0.00000000000001 else ants.t[i][j], end=" ")

    print()
    print()

    # считаем путь
    v = [0, ]
    step = 0
    current = 0
    l = 0
    while step < 4:
        print(current, end=" ")
        step += 1

        temp = current
        value = -1
        for j in range(len(graph)):
            if ants.t[temp][j] > value and j not in v:
                value = ants.t[temp][j]
                current = j

        v.append(current)
        l += graph[temp][current]
    l += graph[current][0]


    print()
    print("Length", l)
