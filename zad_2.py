import matplotlib.pyplot as plt
import numpy as np

def generate_compensated_poisson_process(lam, T, dt):
    n_steps = int(T / dt)
    times = np.linspace(0, T, n_steps)
    increments = np.random.poisson(lam * dt, n_steps)
    trajectory = np.cumsum(increments) - lam * times
    return times, trajectory

lam = 1  # intensywność procesu Poissona
T = 100  # czas trwania procesu
dt = 0.01  # krok czasowy
times, trajectory = generate_compensated_poisson_process(lam, T, dt)

plt.plot(times, trajectory, label='Compensated Poisson Process')
plt.xlabel('Time')
plt.ylabel('Compensated Poisson Process')
plt.title('Compensated Poisson Process Trajectory')
plt.legend()
plt.grid(True)
plt.show()