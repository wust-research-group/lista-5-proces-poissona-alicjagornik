import matplotlib.pyplot as plt
import numpy as np

def proces_poissona(T, lam):
    i = 0
    t = 0
    S = []
    U = []
    N = []
    while t <= T:
        u = np.random.uniform(0, 1)
        t -= 1 / lam * np.log(u)
        i += 1
        S.append(t)
        U.append(i)
    for i in range(len(S) - 1):
        n = S[i + 1] - S[i]
        N.append(n)
    return S, U, N

x_axis, y_axis, N = proces_poissona(10, 1)
print(N)

plt.scatter(x_axis, y_axis)
plt.title('Trajektoria procesu Poissona')
plt.show()
