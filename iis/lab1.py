import math
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter

x_train = [
    # синяя выборка
    [1, 0.52, 0.48],
    [1, 0.5, 0.5],
    [1, 0.69, 0.49],
    [1, 0.36, 0.45],
    [1, 0.46, 0.42],
    [1, 0.52, 0.32],
    [1, 0.55, 0.28],
    [1, 0.57, 0.36],
    [1, 0.65, 0.33],
    [1, 0.695, 0.495],
    [1, 0.41, 0.57],
    [1, 0.5, 0.62],
    [1, 0.51, 0.54],
    [1, 0.62, 0.6],

    # красная выборка
    # левая часть
    [1, 0.38, 0.33],
    [1, 0.37, 0.53],
    [1, 0.45, 0.66],
    [1, 0.55, 0.71],
    [1, 0.69, 0.71],

    [1, 0.12, 0.43],
    [1, 0.18, 0.47],
    [1, 0.22, 0.61],
    [1, 0.11, 0.62],
    [1, 0.23, 0.71],
    [1, 0.28, 0.79],
    [1, 0.4, 0.77],
    [1, 0.48, 0.86],

    [1, 0.05, 0.55],
    [1, 0.05, 0.67],
    [1, 0.12, 0.78],
    [1, 0.24, 0.89],

    # правая часть (отражение)
    [1, 0.6005930879190616, 0.3760574397384784],
    [1, 0.5730173415393354, 0.49331091776335445],
    [1, 0.5477922420942608, 0.3694378782651145],
    [1, 0.4513352163555808, 0.32644154881164344],
    [1, 0.35118170624523337, 0.3581615394771727],
    [1, 0.7105775195797983, 0.4873878829215085],
    [1, 0.6740706615128027, 0.497203843117237],
    [1, 0.667224792393592, 0.46066855234360354],
    [1, 0.7250193401849943, 0.46521619196321806],
    [1, 0.6901624370620391, 0.3790204868134268],
    [1, 0.6810271955670013, 0.29263638315089197],
    [1, 0.5940290225542512, 0.2823183586822014],
    [1, 0.519969238657968, 0.19737027929668027],
    [1, 0.7454474724267853, 0.4944896395711893],
    [1, 0.7670473313387852, 0.44116466257437614],
    [1, 0.7633669741730946, 0.343475412935059],
    [1, 0.7210151792322375, 0.2116677299038311]
]

y_train = [
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

class NN:
    def __init__(self):
        self.x = []
        self.y = None
        self.s = 0.01
        self.c = [5, 10, -50]

    def predict(self, x):
        self.x = x
        self.y = 0
        a = 0
        for i in range(3):
            a += (self.c[i]-self.x[i])**2
        self.y = self.f(math.sqrt(a))

        # return 1 if self.y > 0.5 else 0
        return self.y

    def train(self, x_train, y_train, n, eps):
        for epoch in range(1000000000000000):
            E = 0
            for i in range(len(x_train)):
                _y = self.predict(x_train[i])
                _c = [0, 0, 0]
                _r_s = 0.1
                r_s = 0.1

                E += (y_train[i] - _y)**2

                for j in range(3):
                    _c[j] = self.c[j] + n*(x_train[i][j] - self.c[j])

                    if y_train[i] == 1:
                        _r_s += (x_train[i][j] - self.c[j])**2

                self.c = _c

                # Величину s рассчитываем как расстояние до наиболее отдаленной от центра точки со значением 1
                r_s_ = math.sqrt(_r_s) / (100*(y_train[i] - _y)**2 + 1)
                if y_train[i] == 1 and _y > 0.9:
                    r_s = r_s_


                if r_s > 1:
                    pass
                else:
                    self.s = r_s/2 if r_s/2 > self.s else self.s


            E = E/len(x_train)
            print()
            print(f"Epoch: {epoch}\nError: {E}")
            if E < eps:
                print(E)
                return True

    def f(self, a):
        z = 0.00001 if (2*(self.s**2)) == 0 else (2*(self.s**2))
        return math.exp(-((a**2)/z))



print("--- Start ---")
n = NN()
n.train(x_train, y_train, 0.005, 0.15)

print("--- Train finish ---")
print(n.predict([1, 0.5, 0.5]))
print(n.predict([1, 0.1, 0.3]))
print(n.predict([1, -0.8, 0.1]))
print(n.predict([1, 0.25, 0.27]))
print(n.predict([1, 0.5, 0.2]))
print(n.predict([1, -0.2, 0.5]))
print(n.predict([1, 1, 1]))
print(n.predict([1, 0, 0]))

print(n.c)
print(n.s)


x_s = []
y_s = []
z_s = []

for i in range(100):
    for j in range(100):
        y = n.predict([1, 0.01*i, 0.01*j])

        x_s.append(0.01*i)
        y_s.append(0.01*j)
        z_s.append(y)


fig = plt.figure()
ax = fig.gca(projection='3d')

# Plot the surface
surf = ax.plot_trisurf(np.array(x_s), np.array(y_s), np.array(z_s), cmap=cm.coolwarm, linewidth=0, antialiased=False)

# Customize the z axis
ax.set_zlim(0, 1)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()